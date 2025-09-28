from users import users

def get_all_emails(users: list[dict]) -> list[str]:
    emails = []
    for user in users:
        emails.append(user["email"])
    
    return emails

print(get_all_emails(users))