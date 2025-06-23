from typing import List

from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users
from src.infra.db.entities.users import Users as UsersEntity
from src.infra.db.settings.connection import DBConnectionHandler


class UsersRepository(UsersRepositoryInterface):
    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = UsersEntity(
                    first_name=first_name, last_name=last_name, age=age
                )
                database.session.add(new_registry)
                database.session.commit()

            except Exception:
                database.session.rollback()
                raise Exception

    @classmethod
    def get_user(cls, first_name: str) -> List[Users]:
        with DBConnectionHandler() as database:
            try:
                users = (
                    database.session.query(UsersEntity)
                    .filter(UsersEntity.first_name == first_name)
                    .all()
                )
                return users

            except Exception:
                database.session.rollback()
                raise Exception
