memory_store = {}

def get_memory(user_id: str):

    if user_id not in memory_store:
        memory_store[user_id] = []

    return memory_store[user_id]


def add_message(user_id: str, role: str, content: str):

    memory = get_memory(user_id)

    memory.append({
        "role": role,
        "content": content
    })


def get_conversation_text(user_id: str):

    memory = get_memory(user_id)

    conversation = ""

    for msg in memory:
        conversation += f"{msg['role']}: {msg['content']}\n"

    return conversation
