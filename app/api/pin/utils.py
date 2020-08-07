import hashlib
from random import randint
from faker import Faker

Faker.seed(0)
faker = Faker()


def hash_generator():
    pin = ""
    for num in range(4):
        pin = pin + str(randint(0, 9))

    salt = faker.hexify(text='^^^^^^^^^^', upper=False)
    password = pin + salt

    h = hashlib.sha1(password.encode("utf-8"))

    return {
        "pin": pin,
        "salt": salt,
        "hash": h.digest()
    }
