from users import users

def group_users_by_age(users: list[dict]) -> dict[int, list[dict]]:
    result = dict()

    for user in users:
        age = int(user["age"])

        if age not in result:
            result[age] = []
        result[age].append(user)

    return result

print(group_users_by_age(users))