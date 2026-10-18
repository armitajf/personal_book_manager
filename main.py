from books import show_books, load_books, save_books
from dotenv import load_dotenv
import os

load_dotenv()

name = input("Please enter your name: ")

admin_password = os.getenv("ADMIN_PASSWORD")
open_admin = input("do you want to open admin mode? (yes/no)")

if open_admin.lower() == "yes":
    entered_password = input("enter password : ")
    print("hello admin")
elif open_admin.lower() == "no":
    print("alright")
else:
    print("wrong password")




print(f"welcome, {name} to personal book manager")

books = load_books()

number_of_books = int(input("\nhow many books do you want to add??"))







for i in range(number_of_books):
    book = input(f"please enter a book name {i + 1}: ")
    books.append(book)

save_books(books)



show_books(books)