import React, { useState, useEffect, useRef } from "react";
import Message from "./Message";
import ChatInput from "./ChatInput";
import TypingIndicator from "./TypingIndicator";
import { sendMessage } from "../services/api";

export default function ChatWindow() {

  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "Hello! How can I help you today?"
    }
  ]);

  const [typing, setTyping] = useState(false);

  const messagesEndRef = useRef(null);

  useEffect(() => {
    scrollToBottom();
  }, [messages, typing]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  const handleSend = async (text) => {

    const userMessage = {
      sender: "user",
      text
    };

    setMessages(prev => [...prev, userMessage]);

    setTyping(true);

    try {

      const response = await sendMessage(text);

      setTyping(false);

      const botMessage = {
        sender: "bot",
        text: response
      };

      setMessages(prev => [...prev, botMessage]);

    } catch {

      setTyping(false);

      setMessages(prev => [
        ...prev,
        {
          sender: "bot",
          text: "Error connecting to server"
        }
      ]);
    }
  };

  return (

    <div className="chat-container">

      <div className="chat-header">
        GenAI Assistant
      </div>

      <div className="chat-messages">

        {messages.map((msg, index) => (
          <Message
            key={index}
            sender={msg.sender}
            text={msg.text}
          />
        ))}

        {typing && <TypingIndicator />}

        <div ref={messagesEndRef} />

      </div>

      <ChatInput onSend={handleSend} />

    </div>
  );
}