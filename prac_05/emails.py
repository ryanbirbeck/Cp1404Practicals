"""
Word Occurences
Estimate: 30
Actual: 25
"""


def main():
    """Make a dictionary for emails to names"""
    email_to_name = {}
    email = input("Enter email: ")
    while email != "":
        name = extract_name_from_email(email)
        confirm = input(f"Is your name {name}? (Y/N) ").upper()
        if confirm != "Y" and confirm != "":
            name = input("Enter name: ")
        email_to_name[email] = name
        email = input("Enter email: ")

    max_length = max(len(name) for name in email_to_name)
    for email, name in email_to_name.items():
        print(f"{name:{max_length}} : ({email})")


def extract_name_from_email(email):
    start = email.split('@')[0]
    parts = start.split('.')
    name = " ".join(parts).title()
    return name


main()
