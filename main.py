name = input("Please enter your name: ")
print(f"welcome, {name}")

count = int(input("how many books do you want to add? "))
books = []



for i in range(count):
    book = input("please enter a book name: ")
    books.append(book)

print("your books are: ")

for book in books:
    print(book)