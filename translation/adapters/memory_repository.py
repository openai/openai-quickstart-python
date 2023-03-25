class MemoryRepository(AbstractRepository):
    def __init__(self):
        self._users = list()

    
    def add_user(self, user: User):
        self._users.append(user)
    
    def get_user(self, user_name) -> User:
        return next((user for user in self.__users if user.user_name == user_name), None)
    
    def get_id(self):
        return len(self.__users) + 1