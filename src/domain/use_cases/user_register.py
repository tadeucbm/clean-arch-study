from abc import ABC, abstractmethod
from typing import Dict


class UserRegister(ABC):
    @abstractmethod
    def register(first_name: str, last_name: str, age: int) -> Dict:
        pass
