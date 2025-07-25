from abc import ABC, abstractmethod
from typing import List

from src.domain.models.users import Users


class UsersRepositoryInterface(ABC):
    @abstractmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        pass

    @abstractmethod
    def get_user(cls, first_name: str) -> List[Users]:
        pass
