
# library_management_system.py
# Author: Saptarshi Debnath
# Enhanced Library Management System with Signup & JSON-based credentials

from colorama import Fore, Style, init
import json, os
init(autoreset=True)

CREDENTIALS_FILE = "data/users.json"

# Load credentials
def load_credentials():
    if not os.path.exists(CREDENTIALS_FILE):
        default_creds = {"admin": "admin123", "librarian": "lib123"}
        with open(CREDENTIALS_FILE, "w") as f:
            json.dump(default_creds, f)
        return default_creds
    with open(CREDENTIALS_FILE, "r") as f:
        return json.load(f)

# Save credentials
def save_credentials(credentials):
    with open(CREDENTIALS_FILE, "w") as f:
        json.dump(credentials, f)

credentials = load_credentials()

# Library data
library = {
    "Python Basics": {"author": "Test", "available": True, "issued_to": None},
    "Data Science": {"author": "Test1", "available": False, "issued_to": "John"}
}

# Welcome Screen
def welcome_screen():
    print(Fore.CYAN + Style.BRIGHT + "="*50)
    print(Fore.GREEN + Style.BRIGHT + "      Welcome to the Library Management System")
    print(Fore.CYAN + Style.BRIGHT + "="*50)

# Pause
def pause():
    input(Fore.YELLOW + "\nPress Enter to continue...")

# Display Books
def display_books():
    print("\n" + Fore.CYAN + "--- Library Books ---")
    for title, details in library.items():
        status = "Available" if details["available"] else f"Issued to {details['issued_to']}"
        print(Fore.GREEN + f"Title: {title} | Author: {details['author']} | Status: {status}")

# Add Book
def add_book(title, author):
    if title in library:
        print(Fore.RED + f"The book '{title}' already exists.")
    else:
        library[title] = {"author": author, "available": True, "issued_to": None}
        print(Fore.GREEN + f"The book '{title}' by {author} has been added.")

# Issue Book
def issue_book(title, person_name):
    if title in library:
        if library[title]["available"]:
            library[title]["available"] = False
            library[title]["issued_to"] = person_name
            print(Fore.GREEN + f"The book '{title}' has been issued to {person_name}.")
        else:
            print(Fore.RED + f"The book '{title}' is already issued.")
    else:
        print(Fore.RED + f"The book '{title}' does not exist.")

# Return Book
def return_book(title):
    if title in library:
        if not library[title]["available"]:
            library[title]["available"] = True
            library[title]["issued_to"] = None
            print(Fore.GREEN + f"The book '{title}' has been returned.")
        else:
            print(Fore.RED + f"The book '{title}' was not issued.")
    else:
        print(Fore.RED + f"The book '{title}' does not exist.")

# View Issued Books
def view_issued_books():
    print("\n" + Fore.CYAN + "--- Issued Books ---")
    issued_books = {title: details for title, details in library.items() if not details["available"]}
    if issued_books:
        for title, details in issued_books.items():
            print(Fore.YELLOW + f"Title: {title} | Issued to: {details['issued_to']}")
    else:
        print(Fore.RED + "No books are currently issued.")

# Sign-up
def signup():
    print(Fore.CYAN + "\n--- Sign Up ---")
    new_user = input("Enter new username: ")
    if new_user in credentials:
        print(Fore.RED + "Username already exists. Try logging in.")
        return False
    new_pass = input("Enter new password: ")
    credentials[new_user] = new_pass
    save_credentials(credentials)
    print(Fore.GREEN + "Account created successfully! You can now log in.")
    return True

# Updated login system with signup
def login():
    attempts = 3
    while attempts > 0:
        print("\n1. Login\n2. Sign Up")
        option = input("Choose an option: ")
        if option == "2":
            signup()
            continue
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in credentials and credentials[username] == password:
            print(Fore.GREEN + f"Welcome, {username}!")
            return True
        else:
            attempts -= 1
            print(Fore.RED + f"Incorrect credentials. {attempts} attempts left.")
    print(Fore.RED + "Too many failed attempts. Exiting.")
    return False

# Main Menu
def main_menu():
    if not login():
        return
    while True:
        print("\n" + Fore.MAGENTA + Style.BRIGHT + "--- Library Menu ---")
        print(Fore.CYAN + "1. View Books")
        print("2. Add a Book")
        print("3. Issue a Book")
        print("4. Return a Book")
        print("5. View Issued Books")
        print("6. Exit")

        choice = input(Fore.YELLOW + "Enter your choice: ")

        if choice == "1":
            display_books()
            pause()
        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            add_book(title, author)
            pause()
        elif choice == "3":
            title = input("Enter book title: ")
            person = input("Enter name of the person: ")
            issue_book(title, person)
            pause()
        elif choice == "4":
            title = input("Enter book title: ")
            return_book(title)
            pause()
        elif choice == "5":
            view_issued_books()
            pause()
        elif choice == "6":
            print(Fore.GREEN + "Exiting the system. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")
            pause()

# Run Program
if __name__ == "__main__":
    welcome_screen()
    main_menu()
