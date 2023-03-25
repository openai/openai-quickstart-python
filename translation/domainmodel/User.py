from Message import Message

class User:

    def __init__(self, user_id: int, user_name: str, password: str):
        if type(user_id) is not int or user_id < 0:
            raise ValueError("User ID should be a non negative integer.")
        self.__user_id = user_id

        if type(user_name) is str:
            self.__user_name = user_name.lower().strip()
        else:
            self.__user_name = None


        if isinstance(password, str) and len(password) >= 7:
            self.__password = password
        else:
            self.__password = None
        
        self.__messages = []
    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password
    
    def __repr__(self):
        return f'<User {self.__user_name}, user id = {self.__user_id}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__user_id == other.user_id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return self.__user_id < other.user_id

    def __hash__(self):
        return hash(self.__user_id)
    
    def send_message(self, recipient, content):
        message = Message(self, recipient, content)
        self.messages.append(message)
        recipient.messages.append(message)

    def view_messages(self):
        for message in self.messages:
            print(message)

    def view_messages_with(self, user):
        for message in self.messages:
            if message.sender == user or message.recipient == user:
                print(message)
        