"""IP address format validator using string operations."""


def validate_ip(ip_address):
    """Check the basic format of an IPv4 address.

    Parameter: ip_address (str) - the text entered by the user.
    Returns: True if it has 3 dots, 4 numeric parts, each between 0 and 255;
             otherwise False.
    """
    ip_address = ip_address.strip()  # Remove unnecessary spaces

    # Must contain dots, and exactly three of them
    if "." not in ip_address or ip_address.count(".") != 3:
        return False

    parts = ip_address.split(".")
    if len(parts) != 4:  # Four numbers expected
        return False

    for part in parts:
        try:
            number = int(part)
        except ValueError:  # Non-numeric or empty part such as "one"
            return False
        if number < 0 or number > 255:
            return False
    return True


def main():
    """Ask the user for an IP address and report whether it is valid."""
    ip_address = input("Enter an IP address: ")
    if validate_ip(ip_address):
        print("Valid IP address")
    else:
        print("Invalid IP address")


main()
