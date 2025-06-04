from .user_finder import UserFinder
from src.infra.db.tests.users_repository import UsersRepositorySpy

def test_find():
    first_name = 'meunome'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)

    print(response)

    assert repo.get_user_attributes["first_name"] == first_name
    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"] != []
