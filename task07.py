from users import users

def group_users_by_country(users: list[dict]) -> dict[str, list[dict]]:
    result = dict()

    for user in users:
        country = user["country"]
        if country not in result:
            result[country] = []
        result[country].append(user)

    return result

print(group_users_by_country(users))
