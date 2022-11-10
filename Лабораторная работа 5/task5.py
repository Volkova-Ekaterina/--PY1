import string
from random import sample


def get_random_password(n: int = 8) -> str:
    password_sample = sample(string.ascii_letters+string.digits, n)
    password = ''.join([str(sym) for sym in password_sample])
    return password


print(get_random_password())
