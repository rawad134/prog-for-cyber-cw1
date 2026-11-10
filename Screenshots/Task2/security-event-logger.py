"""Security event logger: records every login attempt until login succeeds."""
import random
from datetime import datetime

VALID_USERNAME = "admin"
VALID_PASSWORD = "Cyber@2026"
IP_ADDRESS = "192.168.1.25"  # Simulated client IP (a console program cannot detect a real one)


def print_event_log(username, event):
    """Print one event log entry.

    Parameters: username (str) - name entered; event (str) - event description.
    """
    event_id = random.randint(1000, 9999)
    timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print("\n----- Security Event Log -----")
    print(f"Event ID: {event_id}")
    print(f"Username: {username}")
    print(f"IP Address: {IP_ADDRESS}")
    print(f"Event: {event}")
    print(f"Timestamp: {timestamp}")
    print("------------------------------\n")


def main():
    """Repeat the login prompt until the correct credentials are entered."""
    logged_in = False
    while not logged_in:
        username = input("Username: ").strip()
        password = input("Password: ")

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            print_event_log(username, "Successful login")
            logged_in = True
        else:
            print_event_log(username if username else "(blank)", "Failed login")

    print("Welcome! Login successful.")


main()
