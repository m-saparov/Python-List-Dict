from users import users

def get_unique_countries(users: list[dict]) -> list[str]:
    countries = set()
    for user in users:
        countries.add(user["country"])
    
    return countries

print(get_unique_countries(users))
