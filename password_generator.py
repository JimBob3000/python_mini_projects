import random
import string


def generate_password():
    # Using a-z, A-Z and 0-9
    options = string.ascii_letters + string.digits

    # Pick 18 characters from options at random and put into a string
    password = "".join(random.choices(options, k=18))

    return password


print(f"New password: {generate_password()}")
