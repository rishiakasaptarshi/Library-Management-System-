from colorama import Fore, Style, init
from pathlib import Path
import json
import os
import getpass

init(autoreset=True)

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

CREDENTIALS_FILE = DATA_DIR / "users.json"
LIBRARY_FILE = DATA_DIR / "library.json"


class LibraryManagementSystem:
    def __init__(self):
        self.credentials = self.load_credentials()
        self.library = self.load_library()

    def load_credentials(self):
        """Load user credentials from JSON file or create default."""
        if not CREDENTIALS_FILE.exists():
            default_creds = {"admin": "admin123", "librarian": "lib123"}
            self.save_json(CREDENTIALS_FILE, default_creds)
            return default_creds
        return self.load_json(CREDENTIALS_FILE)

    def save_credentials(self):
        """Save user credentials to JSON file."""
        self.save_json(CREDENTIALS_FILE, self.credentials)

    def load_library(self):
        """Load library data from JSON or initialize default."""
        if not LIBRARY_FILE.exists():
            default_library = {
                "Python Basics": {"author": "Test", "available": True, "issued_to": None},
                "Data Science": {"author": "Test1", "available": False, "issued_to": "John"}
            }
            self.save_json(LIBRARY_FILE, default_library)
            return default_library
        return self.load_json(LIBRARY_FILE)

    def save_library(self):
        """Save library data to JSON file."""
        self.save_json(LIBRARY_FILE, self.library)

    @staticmethod
    def load_json(file_path):
        with open(file_path, "r") as f:
            return json.load(f)

    @staticmethod
    def save_json(file_path, data):
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

    def welcome_screen(self):
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)
        print(Fore.GREEN + Style.BRIGHT + "      Welcome to the Library Management System")
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)

    @staticmethod
    def pause():
        input(Fore.YELLOW + "\nPress Enter to continue...")

    def display_books(self):
        print("\n" + Fore.CYAN + "--- Library Books ---")
        if not self.library:
            print(Fore.RED + "No books in the library.")
            return
        for title, details in self.library.items():
            status = "Available" if details.get("available", True) else f"Issued to {details.get('issued_to')}"
            print(Fore.GREEN + f"Title: {title} | Author: {details.get('author', 'Unknown')} | Status: {status}")

    def add_book(self, title, author):
        if title in self.library:
            print(Fore.RED + f"The book '{title}' already exists.")
        else:
            self.library[title] = {"author": author, "available": True, "issued_to": None}
            self.save_library()
            print(Fore.GREEN + f"The book '{title}' by {author} has been added.")

    def issue_book(self, title, person_name):
        book = self.library.get(title)
        if not book:
            print(Fore.RED + f"The book '{title}' does not exist.")
            return
        if book.get("available", True):
            book["available"] = False
            book["issued_to"] = person_name
            self.save_library()
            print(Fore.GREEN + f"The book '{title}' has been issued to {person_name}.")
        else:
            print(Fore.RED + f"The book '{title}' is already issued.")

    def return_book(self, title):
        book = self.library.get(title)
        if not book:
            print(Fore.RED + f"The book '{title}' does not exist.")
            return
        if not book.get("available", True):
            book["available"] = True
            book["issued_to"] = None
            self.save_library()
            print(Fore.GREEN + f"The book '{title}' has been returned.")
        else:
            print(Fore.RED + f"The book '{title}' was not issued.")

    def view_issued_books(self):
        print("\n" + Fore.CYAN + "--- Issued Books ---")
        issued_books = {title: book for title, book in self.library.items() if not book.get("available", True)}
        if issued_books:
            for title, details in issued_books.items():
                print(Fore.YELLOW + f"Title: {title} | Issued to: {details.get('issued_to')}")
        else:
            print(Fore.RED + "No books are currently issued.")

    def signup(self):
        print(Fore.CYAN + "\n--- Sign Up ---")
        while True:
            new_user = input("Enter new username: ").strip()
            if not new_user:
                print(Fore.RED + "Username cannot be empty.")
                continue
            if new_user in self.credentials:
                print(Fore.RED + "Username already exists. Try logging in.")
                return False
            break

        while True:
            new_pass = getpass.getpass("Enter new password: ").strip()
            if not new_pass:
                print(Fore.RED + "Password cannot be empty.")
                continue
            break

        self.credentials[new_user] = new_pass
        self.save_credentials()
        print(Fore.GREEN + "Account created successfully! You can now log in.")
        return True

    def login(self):
        attempts = 3
        while attempts > 0:
            print("\n1. Login\n2. Sign Up")
            option = input("Choose an option: ").strip()
            if option == "2":
                self.signup()
                continue
            if option != "1":
                print(Fore.RED + "Invalid option. Please try again.")
                continue

            username = input("Enter username: ").strip()
            password = getpass.getpass("Enter password: ").strip()
            if self.credentials.get(username) == password:
                print(Fore.GREEN + f"Welcome, {username}!")
                return True
            else:
                attempts -= 1
                print(Fore.RED + f"Incorrect credentials. {attempts} attempts left.")
        print(Fore.RED + "Too many failed attempts. Exiting.")
        return False

    def main_menu(self):
        if not self.login():
            return
        while True:
            print("\n" + Fore.MAGENTA + Style.BRIGHT + "--- Library Menu ---")
            print(Fore.CYAN + "1. View Books")
            print("2. Add a Book")
            print("3. Issue a Book")
            print("4. Return a Book")
            print("5. View Issued Books")
            print("6. Exit")

            choice = input(Fore.YELLOW + "Enter your choice: ").strip()
            if choice == "1":
                self.display_books()
                self.pause()
            elif choice == "2":
                title = input("Enter book title: ").strip()
                author = input("Enter author name: ").strip()
                self.add_book(title, author)
                self.pause()
            elif choice == "3":
                title = input("Enter book title: ").strip()
                person = input("Enter name of the person: ").strip()
                self.issue_book(title, person)
                self.pause()
            elif choice == "4":
                title = input("Enter book title: ").strip()
                self.return_book(title)
                self.pause()
            elif choice == "5":
                self.view_issued_books()
                self.pause()
            elif choice == "6":
                print(Fore.GREEN + "Exiting the system. Goodbye!")
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")
                self.pause()


if __name__ == "__main__":
    system = LibraryManagementSystem()
    system.welcome_screen()
    system.main_menu()
