
import secrets
import string

def local_password(length=5, num=1, characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:,.<>/?"):

    passwords = []
    for _ in range(num):
        password = ''.join(secrets.choice(characters) for _ in range(length))
        passwords.append(password)
    return passwords

# Example usage
pw = local_password(10,1)
# print(f"Randomly generatd password for you: {pw}")

