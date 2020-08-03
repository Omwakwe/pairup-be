import secrets
import string


def generate_password(length):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    print("Random string of length", length, "is:", password)
    return password