from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users
from typing import Dict, List

class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        self.__validate_name(first_name)
        users = self.__search_user(first_name)
        response = self.__format_response(users)
        return response

    @classmethod
    def __validate_name(cls, first_name:str) -> None:
        if not first_name.isalpha():
            raise Exception("Nome inválido para busca")

        if len(first_name) > 18:
            raise Exception("Nome muito grande para busca")

    def __search_user(self, first_name: str) -> List[Users]:
        users = self.__users_repository.get_user(first_name)
        if users == []:
            raise Exception("Usuário não encontrado")
        return users

    @classmethod
    def __format_response(cls, users: List[Users]) -> Dict:
        attributes = []
        for user in users:
            attributes.append(
                {"first_name": user.first_name, "age": user.age}
            )

        response = {
            "type": "Users",
            "count": len(users),
            "attributes": users
        }

        return response
