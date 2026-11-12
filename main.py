from books import show_books, load_books, save_books
from dotenv import load_dotenv
import os

load_dotenv()

name = input("Please enter your name: ")

admin_password = os.getenv("ADMIN_PASSWORD")
open_admin = input("Do you want to open admin mode? (yes/no): ")

if open_admin.lower() == "yes":
    entered_password = input("Enter password: ")

    if entered_password == admin_password:
        print("Hello admin")
    else:
        print("Wrong password")

elif open_admin.lower() == "no":
    print("Alright")
else:
    print("Invalid answer")

print(f"Welcome, {name} to Personal Book Manager")

books = load_books()

number_of_books = int(input("\nHow many books do you want to add? "))

for i in range(number_of_books):
    book_name = input(f"Please enter book name {i + 1}: ")

    priority = input("Enter priority (low/medium/high): ").lower()

    while priority not in ["low", "medium", "high"]:
        print("Invalid priority!")
        priority = input("Enter priority (low/medium/high): ").lower()

    books.append({
        "name": book_name,
        "priority": priority
    })

save_books(books)

show_books(books)

print(len(books))
