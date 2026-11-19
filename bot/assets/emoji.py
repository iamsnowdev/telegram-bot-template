class Emoji:
    def __init__(self, emoji_id: str, emoji: str):
        self.emoji_id = emoji_id
        self.html = f"<tg-emoji emoji-id=\"{emoji_id}\">{emoji}</tg-emoji>"