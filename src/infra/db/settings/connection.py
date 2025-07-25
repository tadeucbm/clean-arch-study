from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import Settings


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = Settings().DATABASE_URL
        self.__engine = self.__create_database_engine()
        self.__session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.session.close()
