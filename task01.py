from users import users

def get_all_names(users: list[dict]) -> list[str]:
    names = []
    for user in users:
        names.append(user["name"])
    
    return names

print(get_all_names(users))