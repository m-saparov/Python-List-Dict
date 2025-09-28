from users import users

def get_all_email_domains(users: list[dict]) -> list[str]:
    domains = set() # bu takrorlansa chiqarmaydi. listga o'tkazsak hammasi chiqadi
    for user in users:
        email = user["email"].split("@")
        domains.add(email[1])   # listda bo'lsa append qilamiz

    return domains

print(get_all_email_domains(users))
