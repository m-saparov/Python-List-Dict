from users import users

def get_users_in_age_range(users: list[dict], min_age: int, max_age: int) -> list[dict]:
    result = []

    for user in users:
        if user["age"] >= min_age and user["age"] <= max_age:
            result.append(user)

    return result

print(get_users_in_age_range(users, 30, 35))