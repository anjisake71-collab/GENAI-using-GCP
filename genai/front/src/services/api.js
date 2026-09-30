const API_URL =
"https://genai-backend-249547597952.us-central1.run.app/chat";

export async function sendMessage(message) {

  const response = await fetch(API_URL, {

    method: "POST",

    headers: {
      "Content-Type": "application/json"
    },

    body: JSON.stringify({
      message: message,
      user_id: "user123"
    }),

  });

  const data = await response.json();

  return data.response;
}