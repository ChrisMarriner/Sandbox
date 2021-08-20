"""
Christopher Marriner
CP1404 - Password Checker
"""

MINIMUM_LENGTH = 4


def main():
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        password = input("Password needs to be at least {} characters: ".format(MINIMUM_LENGTH))
    print('*' * len(password))


main()
