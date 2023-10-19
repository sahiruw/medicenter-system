import hashlib
import secrets
import string

def generate_random_password(length=12):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password


def hash_password(user_password):
    hashed_password = hashlib.md5()
    hashed_password.update(user_password.encode("utf-8"))
    return hashed_password.hexdigest()
