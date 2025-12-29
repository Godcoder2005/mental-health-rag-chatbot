CRISIS_KEYWORDS = [
    "kill myself",
    "suicide",
    "end my life",
    "self harm",
    "hurt myself",
    "i want to die"
]

def is_crisis(message: str) -> bool:
    message = message.lower()
    return any(k in message for k in CRISIS_KEYWORDS)
