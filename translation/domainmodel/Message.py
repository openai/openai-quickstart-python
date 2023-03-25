class Message:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content

    def __str__(self):
        return f"{self.sender.name} -> {self.recipient.name}: {self.content}"