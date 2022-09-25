def main():
    get_password()


def get_password():
    password = str(input("Enter password: "))
    minimum_length = 10
    if len(password) >= minimum_length:
        print_password(password)
    else:
        print('Invalid password')


def print_password(password):
    print('*' * len(password))


main()
