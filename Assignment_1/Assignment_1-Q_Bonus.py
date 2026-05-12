import os
import shutil
from datetime import datetime

def toolkit():
    print("\n=== Cyber Safety Toolkit ===")

    print("1. Password Checker")
    print("2. File Backup Tool")
    print("3. Log Analyzer")
    print("4. Exit")

    choice = input("Select an option: ")

    # Password Strength Checker
    if choice == "1":

        password = input("Enter Password: ")

        score = sum([
            len(password) >= 8,
            any(c.isdigit() for c in password),
            any(c.islower() for c in password),
            any(c.isupper() for c in password)
        ])

        strength = ["Weak", "Medium", "Strong", "Very Strong"]

        print(f"Password Strength: {strength[score-1]}")

    # File Backup Tool
    elif choice == "2":

        file_name = input("Enter file name to backup: ")

        if os.path.exists(file_name):

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            backup_file = f"{file_name}_{timestamp}.bak"

            shutil.copy(file_name, backup_file)

            print(f"Backup created: {backup_file}")

        else:
            print("File not found")

    # Log Analyzer
    elif choice == "3":

        logs = [
            "Failed password for root",
            "Accepted password for user",
            "Failed login attempt from admin"
        ]

        failed = [log for log in logs if "Failed" in log]

        print("\nFailed Login Attempts:")

        for log in failed:
            print(log)

    # Exit
    elif choice == "4":
        print("Exiting Toolkit")

    else:
        print("Invalid Choice")

toolkit()
