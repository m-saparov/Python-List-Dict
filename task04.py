from users import users

def find_user_by_phone(users: list[dict], phone: str) -> dict | None:
    for user in users:
        if user["phone"] == phone:
            return user

    return None

print(find_user_by_phone(users, "+998901002223")) # None
print(find_user_by_phone(users, "+998901112223")) #{"name": "Kamol", "email": "kamol8@mail.ru", "age": 22, "phone": "+998901112223", "country": "Germany"},
