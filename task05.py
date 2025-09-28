from users import users

def find_user_by_email(users: list[dict], email: str) -> dict | None:
    for user in users:
        if user["email"] == email:
            return user
        
    return None

print(find_user_by_email(users, "ali@mail.ru")) #None
