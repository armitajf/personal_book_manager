# Personal Book Manager
A simple book managment project built with python

## Features
- Add multiple books
- Display all books
- Save books in a JSON file
- Load previously saved books
- Admin mode
- Add priority levels to books

## Requirements
- Python
- python-dotenv

## Installation
Install the required packages:

```bash
python -m pip install -r requirments.txt
```

## Envoirment setup
create a `.env` file in the project folder

Use `.env.example` as s template

Add your admin password

```env
admin_password=your_password_here
```

replace `your_password_here` with your own admin password


## run the program
run the main file
```bash
python main.py
```

## Screenshots
![personal_task_manager_screenshots](images\img.png)


## Project Structure
```text
personal_book_manager/
│
├── main.py              
├── books.py              
├── books.json           
├── .gitignore            
├── .env                 
├── .env.example         
├── requirements.txt     
├── images/              
└── README.md            
```


## How It Works

1. The program starts and asks the user `for` their name.
2. It displays a welcome message.
3. The program loads previously saved books from books.json.
4. The user can choose how many `new` books to add.
5. The program receives information about each book.
6. The `new` books are added to the book list.
7. The program displays the updated list of books.
8. All book information is saved in books.json.
9. The user can enter Admin Mode by providing the correct password.
10. The admin password is loaded from the .env file.



## Troubleshooting

### 1. FileNotFoundError

- Meaning: The program cannot find the required file.
- Reason: The file may not exist in the project folder.
- Check: Make sure the file name and project path are correct.

### 2. JSONDecodeError

- Meaning: Python cannot read the JSON file.
- Reason: The books.json file may be empty or contain incorrect JSON data.
- Check: Open books.json and check its content and format.

### 3. ModuleNotFoundError: dotenv

- Meaning: Python cannot find the dotenv module.
- Reason: The python-dotenv package may not be installed.
- Check: Install the required packages using pip install -r requirements.txt.

### 4. Admin Password Not Working

- Meaning: The program cannot read or verify the admin password correctly.
- Reason: The password may be missing or incorrectly written in the .env file.
- Check: Make sure the .env file exists and BOOK_MANAGER_ADMIN_PASSWORD is written correctly.


## Book Priority
Each book can have one of three priority levels:
- low
- medium
- high





























































































































































































































































































































































































































































