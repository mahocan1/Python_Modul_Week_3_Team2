# Python_Modul_Week_3

Question1: Create a Python class called "Rectangle" that represents a rectangle. The Rectangle class must have the following properties and methods:
##### Features:
- width (an integer)
- height (an integer)
##### Methods:
- area(self): A method that calculates and returns the area of ​​the rectangle.
- perimeter(self): A method that calculates and returns the perimeter of the rectangle.
- Create an instance of Rectangle class, set its width to 5 and height to 7, then print its area and perimeter.
##
Question2: Create a "School" class in Python. This class should have the following features and functionality:

##### Features:
- "name"
- "foundation_year"
- "students"
- "teachers"
-
##### Methods:
- add_new_student(self, student_name, class): A method used to add a new student to the school. It takes the student's name and class and adds it to the "students" list.
- add_new_teacher(self, teacher_name, branch): A method used to add a new teacher to the school. It takes the teacher's name and major and adds it to the "teachers" dictionary.
- view_student_list(self): A method used to display the list of students enrolled in the school. List student names and classes.
- view_teacher_list(self): A method used to display the list of teachers working in the school. List teacher names and majors.
##
Question3: Create a "Shape" class. Under this class, create two subclasses, the "Rectangle" and "Square" classes.

- Let the "shape" class have two properties: "width" and "height."
- Let the "Rectangle" class inherit from the "Shape" class and add an additional "calculate_area()" method.
- Let the "Square" class inherit from the "Shape" class and calculate the area of ​​the square using the same "area_calculate()" method.
- Create a "Rectangle" and a "Square" instance, determine the width and height of each, and calculate the area of ​​each and print the results.
##
Question4: Create a "Vehicle" class in Python. Make sure this class has the following properties:

##### Features:
- "make" (Brand of vehicle)
- "model" (Vehicle model)
- "year" (Year of manufacture of the vehicle)

Create a "Vehicle" class and create two derived subclasses, "Off-Road Vehicle" (SUV) and "SportsCar" classes.

- The "Off-Road Vehicle" class inherits from the "Vehicle" class and adds an additional "four_wheel drive" feature.
- Let the "SportCar" class inherit from the "Vehicle" class and add a "max_speed" property.

Create an instance of each class, determine its properties, and write a program to display these properties.
##
 Question5: Create a "Customer" class and an "Account" class. Let the "Account" class inherit from the "Customer" class and represent a customer's bank account information.

##### Customer Class Features:
- "name" (customer name)
- "surname" (customer surname)
- "tc_identification" (customer TR ID number)
- "phone" (customer phone number)

##### Account Class Properties:
- "customer" (a Customer object)
- "account_number" (account number)
- "balance" (account balance)

##### Customer Class Method:
- "display_information()": Displays the customer's name, surname, TR ID number and telephone number.

##### Account Class Methods:
- "deposit(self, amount)": A method that deposits a certain amount of money into the account.
- "money_check(self, amount)": A method that withdraws a certain amount of money from the account. However, if there is not enough balance in the account, the transaction should not occur and a message should be displayed.
- "display_balance()": A method that displays the account balance.

Create these two classes, then create a Customer object and an Account object, add the customer information to the Account object, and perform account operations and view the results.

## Mini Project
# 📚 Library Management System

A simple **Library Management System** written in Python.  
It allows users to borrow and return books, manage accounts, and store data in a JSON file so the system continues from where it left off.

---

## 🚀 Features
- User login & account creation  
- Borrow and return books  
- View all available books  
- Track borrowed books  
- Data persistence with JSON (save & load)

---

## 🏗️ Class Design

### `Book` (base class)
**Attributes**
- `title`
- `author`
- `publication_year`
- `is_borrowed`
- `borrowed_by`

**Methods**
- `show_info()`
- `borrow(user)`
- `return_book()`
- `to_dict()`

---

### `Novel` (inherits `Book`)
- Additional attribute: `genre`

### `Magazine` (inherits `Book`)
- Additional attribute: `issue`

---

### `User`
**Attributes**
- `name`
- `password`
- `borrowed_books`

**Methods**
- `borrow_book(book)`
- `return_book(book)`
- `list_borrowed_books()`
- `to_dict()`

---

### `Library`
**Attributes**
- `name`
- `books`
- `users`

**Methods**
- `add_book(book)`
- `add_user(user)`
- `show_all_books()`
- `login(name, password)`
- `save(file)` → saves all data to JSON  
- `load(file)` → loads data from JSON and restores relationships

---

## 📋 Program Flow

1. On startup, a **login screen** is shown.  
2. The user can log in or create a new account.  
3. Menu options:
- 1 - List all books
- 2 - Borrow a book
- 3 - Return a book
- 4 - Show my borrowed books
- 5 - Save and exit

4. On exit, all data is saved to a JSON file.  
5. On the next run, the system loads the saved state and continues.

---

## 💾 Persistence
- All books, users, and borrowing states are stored in a **JSON file**.  
- When the program restarts, the data is reloaded so nothing is lost.

---


## HackerRank Questions

* **Inheritance:** https://www.hackerrank.com/challenges/inheritance/problem

* **Classes: Dealing with Complex Numbers:** https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
