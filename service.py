import json

from .main import User

def authenticate(user_id: str):

    try:
        with open("users_table.json", mode="r", encoding="utf-8") as f:
            users = json.load(f)
    except FileExistsError:
        return None

    user = users.get(user_id)
    if not user:
        return None
    return  User(**user)
