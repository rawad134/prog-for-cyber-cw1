"""Reusable cyber security helper functions."""
import random
import string

MIN_PASSWORD_LENGTH = 8
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>?"


def validate_password(password):
    """Check a password for minimum length and variety.

    Parameter: password (str).
    Returns: True if it is at least 8 characters and has a letter, digit and symbol.
    """
    if len(password) < MIN_PASSWORD_LENGTH:
        return False
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in SYMBOLS for char in password)
    return has_letter and has_digit and has_symbol


def check_ip_address(ip_address):
    """Check IP format: three dots, four numbers, each in the range 0-255.

    Parameter: ip_address (str).
    Returns: True if the format is valid, otherwise False.
    """
    parts = ip_address.strip().split(".")
    if len(parts) != 4:  # Four parts means exactly three dots
        return False
    for part in parts:
        try:
            if not 0 <= int(part) <= 255:
                return False
        except ValueError:
            return False
    return True


def generate_strong_password():
    """Generate a random password of 10-16 characters with mixed character types.

    Returns: the generated password (str).
    """
    length = random.randint(10, 16)  # Random length each time
    # Guarantee at least one character of each type
    characters = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(SYMBOLS),
    ]
    all_characters = string.ascii_letters + string.digits + SYMBOLS
    while len(characters) < length:
        characters.append(random.choice(all_characters))
    random.shuffle(characters)  # Hide the guaranteed characters' positions
    return "".join(characters)


if __name__ == "__main__":
    print("Testing password validation:")
    print(validate_password("Abc123!@"))

    print("\nTesting IP validation:")
    print(check_ip_address("192.168.1.1"))

    print("\nTesting password generation:")
    print(generate_strong_password())


