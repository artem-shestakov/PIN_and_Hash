import hashlib
from random import randint
from faker import Faker

Faker.seed(0)
faker = Faker()


# Generate PIN code, salt and SHA-1 hash pin+salt
def hash_generator(pin_len, salt_len):
    # Create PIN code
    pin = ""
    for num in range(pin_len):
        pin = pin + str(randint(0, 9))

    # Generate random salt
    salt = faker.hexify(text=f'^'*salt_len, upper=False)
    password = pin + salt

    # Getting hash
    h = hashlib.sha1(password.encode("utf-8"))
    return {
        "pin": pin,
        "salt": salt,
        "hash": h.hexdigest().upper()
    }
