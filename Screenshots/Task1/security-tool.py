"""Basic security tool: authentication followed by a security menu."""

STORED_USERNAME = "admin"
STORED_PASSWORD = "Cyber@2026"
MAX_LOGIN_ATTEMPTS = 3


def login():
    """Ask for credentials up to MAX_LOGIN_ATTEMPTS times.

    Returns True if authentication succeeds, False if the account is frozen.
    """
    failed_logins = 0
    while failed_logins < MAX_LOGIN_ATTEMPTS:
        username = input("Username: ").strip()
        password = input("Password: ")
        if username == STORED_USERNAME and password == STORED_PASSWORD:
            print("Authentication succeeded.")
            return True
        failed_logins += 1
        print(f"Authentication failed ({failed_logins}/{MAX_LOGIN_ATTEMPTS}).")
    print("Too many failed logins. The account is frozen for 24 hours.")
    return False


def security_event_counter():
    """Ask for a password 10 times, count results and raise an alert if needed."""
    correct_password = "Secure#123"
    total_attempts = 10
    correct_count = 0
    incorrect_count = 0

    for attempt in range(1, total_attempts + 1):
        guess = input(f"Attempt {attempt}/{total_attempts} - enter password: ")
        if guess == correct_password:
            correct_count += 1
        else:
            incorrect_count += 1

    incorrect_percentage = incorrect_count / total_attempts * 100
    print(f"Correct: {correct_count}")
    print(f"Incorrect: {incorrect_count}")
    print(f"Incorrect percentage: {incorrect_percentage:.1f}%")
    if incorrect_percentage > 50:
        print("ALERT: More than 50% of password attempts were incorrect!")


def brute_force_simulation():
    """Let the user guess a predefined password within a maximum number of attempts."""
    secret_password = "Dragon42!"
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        guess = input("Guess the password: ")
        attempts += 1  # Count every guess
        if guess == secret_password:
            print(f"Password cracked in {attempts} attempt(s).")
            return
        print(f"Wrong guess. Attempts left: {max_attempts - attempts}")
    print("Maximum number of attempts reached. Simulation stopped.")


def show_menu():
    """Display the security menu."""
    print("\n--- Security Menu ---")
    print("1. Security Event Counter")
    print("2. Brute-Force Simulation")
    print("3. Login Authentication")
    print("4. Exit")


def main():
    """Authenticate the user, then run the menu until Exit is chosen."""
    if not login():
        return

    while True:
        show_menu()
        try:
            choice = int(input("Choose an option (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            security_event_counter()
        elif choice == 2:
            brute_force_simulation()
        elif choice == 3:
            login()
        elif choice == 4:
            print("Thank you for using the security tool")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3 or 4.")


main()


