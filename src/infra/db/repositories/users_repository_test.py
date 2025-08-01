import pytest
from sqlalchemy import text

from src.infra.db.settings.connection import DBConnectionHandler

from .users_repository import UsersRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


@pytest.mark.skip(reason='Sensive test')
def test_add_user():
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_age = 34

    users_repository = UsersRepository()
    users_repository.insert_user(
        mocked_first_name, mocked_last_name, mocked_age
    )

    sql = """
        SELECT * FROM users
        WHERE first_name = '{}'
        AND last_name = '{}'
        AND age = {}
    """.format(mocked_first_name, mocked_last_name, mocked_age)

    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age

    connection.execute(text(f"""DELETE FROM users WHERE id = {registry.id}"""))
    connection.commit()


@pytest.mark.skip(reason='Sensive test')
def test_select_user():
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_age = 34

    users_repository = UsersRepository()
    users_repository.insert_user(
        mocked_first_name, mocked_last_name, mocked_age
    )

    registry = users_repository.get_user(mocked_first_name)[0]

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age

    connection.execute(text(f"""DELETE FROM users WHERE id = {registry.id}"""))
    connection.commit()
