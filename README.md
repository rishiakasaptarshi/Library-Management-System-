
# Library Management System

A **Python-based Library Management System (LMS)** designed to manage basic library operations. This project allows a librarian or admin to **add, issue, return, and track books**, along with viewing the list of issued books and their borrowers.

---

## **Project Introduction**
This enhanced version includes:
- **Sign-Up System**: New users can create their own accounts.
- **JSON-based Credential Storage**: User accounts are stored in a `users.json` file.
- **Professional Folder Structure** for GitHub.

---

## **Project Structure**
```
Library-Management-System/
├── src/
│   └── library_management_system.py     # Main program
├── data/
│   └── users.json                       # User credentials
├── docs/
│   └── screenshot.png                   # Screenshot of program
├── README.md                            # Project documentation
├── requirements.txt                     # Dependencies
└── LICENSE                              # Open-source license
```

---

## **Features**
- **Login & Signup System**: Secure access with predefined credentials and ability to create new accounts.
- **Book Management**: Add new books, check availability, and manage inventory.
- **Issue & Return Books**: Track borrowed books with borrower details.
- **Issued Books View**: Quickly view which books are currently issued and to whom.
- **Interactive Menu**: A user-friendly console interface (with colored text using `colorama`).

---

## **How to Run**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Library-Management-System.git
   ```
2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the program:
   ```bash
   python src/library_management_system.py
   ```

---

## **Tech Stack**
- **Programming Language**: Python
- **Libraries**: `colorama`
- **Data Storage**: `JSON`

---

## **Author**
**Saptarshi Debnath**  
[LinkedIn](https://www.linkedin.com/in/saptarshi-debnath-64a444190/) | [GitHub](https://github.com/rishiakasaptarshi)
