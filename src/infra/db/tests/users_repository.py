from src.domain.models.users import Users
from typing import List

class UsersRepositorySpy:

    def __init__(self):
        self.insert_user_atributes = {}
        self.get_user_attributes = {}

    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_atributes["first_name"] = first_name
        self.insert_user_atributes["last_name"] = last_name
        self.insert_user_atributes["age"] = age
        return

    def get_user(self, first_name: str) -> List[Users]:
        self.get_user_attributes["first_name"] = first_name
        return [
            Users(23, first_name, 'last', 43),
            Users(23, first_name, 'last_2', 12)
        ]
