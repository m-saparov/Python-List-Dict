from users import users

def get_min_max_age_users(users: list[dict]) -> tuple[dict, dict]:
    young_user = users[0]
    old_user = users[0]

    for user in users:
        if young_user["age"] > user["age"]:
            young_user = user
        if old_user["age"] < user["age"]:
            old_user = user
    
    return (young_user, old_user)


print(get_min_max_age_users(users))
