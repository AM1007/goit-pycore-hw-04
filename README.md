## Working with files and the modular system.

### Task 1

You have a text file that contains information about the monthly salaries of developers in your company. Each line in the file contains the developer's last name and salary, separated by a comma with no spaces.

Example:

```python
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
```

Your task is to design a function `total_salary(path)` that parses this file and returns the total and average salary of all developers.

#### Task requirements:

1. The `total_salary(path)` function must accept one argument - the path to the text file `(path)`.
2. The file contains data about developer salaries, separated by commas. Each row indicates one developer.
3. The function should analyze the file, calculate the total and average amount of wages.
4. The result of the function is a tuple of two numbers: the total amount of salaries and the average salary.

#### Recommendations for implementation:

1. Use the `with` context manager to read files.
2. Remember to set the encoding when opening files
3. To split the data in each row, you can use the split(',') method.
4. Calculate the total salary and then divide it by the number of developers to get the average salary.
5. Handle possible exceptions when working with files, such as the missing file.

#### Example of using the function:

```python
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
```

#### Expected result:

```python
Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000
```

---

### Task 2

You have a text file that contains information about cats. Each line of the file contains the cat's unique identifier, its name, and its age, separated by a comma. Example:

```python
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
```

Your task is to design a function get_cats_info(path) that reads this file and returns a list of dictionaries with information about each cat.

#### Task requirements:

1. The function `get_cats_info(path)` must accept one argument - the path to the text file `(path)`.
2. The file contains data about cats, where each record contains a unique identifier, the cat's name and its age.
3. The function should return a list of dictionaries where each dictionary contains information about one cat.

#### Recommendations for implementation:

1. Use `with` to read the file safely.
2. Remember to set the encoding when opening files
3. For each line in the file, use `split(',')` to get the cat's ID, name, and age.
4. Create a dictionary with the keys `"id"`, `"name"`, `"age"` for each cat and add it to the list to be returned.
5. Handle possible exceptions related to reading the file.

#### Example of using the function:

```python
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
```

#### Expected result:

```python
[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]
```

---

### Task 3

Develop a script that accepts a directory path as a command line argument and visualizes the structure of that directory, outputting the names of all subdirectories and files. For better visual perception, the names of directories and files should differ in color.

#### Task requirements:

1. Create a virtual Python environment to isolate project dependencies.
2. The script must receive the directory path as an argument when running. This path specifies where the directory whose structure is to be displayed is located.
3. Using the `colorama` library to implement color output.
4. The script must correctly display both directory names and file names, using a recursive method of directory traversal (you can, if you wish, use a non-recursive method).
5. There should be validation and error handling, for example if the specified path does not exist or does not point to a directory.

#### Example of use:

If you execute the script and pass it the absolute path to the directory as a parameter.

```python
python hw03.py /шлях/до/вашої/директорії
```

This will cause the terminal to list all the subdirectories and files in the specified directory, using different colors for the subdirectories and files, making it easier to visually understand the file structure.

For a directory with the following structure

```python
📦picture
 ┣ 📂Logo
 ┃ ┣ 📜IBM+Logo.png
 ┃ ┣ 📜ibm.svg
 ┃ ┗ 📜logo-tm.png
 ┣ 📜bot-icon.png
 ┗ 📜mongodb.jpg
```

The script should output a similar structure

```python
picture/
    bot-icon.png
    Logo/
        IBM+Logo.png
        ibm.svg
        logo-tm.png
    mongodb.jpg
```

---

### Task 4

Write a helper console bot that will recognize commands entered from the keyboard and respond accordingly.

> [!IMPORTANT] ☝ The assistant bot should become for us the prototype of the assistant application that we will develop in the following homework. In the first approximation, the assistant application should be able to work with the contact book and calendar.

In this homework, we will focus on the interface of the bot itself. The simplest and most convenient interface at the initial stage of development is the CLI (Command Line Interface) console application. The CLI is simple enough to implement.

Any CLI consists of three main elements:

- **Command parser.** The part responsible for parsing strings entered by the user, extracting keywords and command modifiers from the string.
- **Functions command handlers** - a set of functions, also called handler, they are responsible for the direct execution of commands.
- **A request-response cycle.** This part of the application is responsible for receiving data from the user and returning the response from the handler function to the user.

At the first stage, our bot-assistant must be able to save a name and a phone number, find a phone number by name, change the recorded phone number, display all the saved records in the console. To implement such simple logic, we will use a dictionary. In the dictionary, we will store the username as the key and the phone number as the value.

#### Recommendations for implementation

First, we need to systematize the description of our command formats for the console helper bot. This will help to understand what functions should be done for each team. Let's do this:

1. The `"hello"` command, here you can do without the function and use the usual print:

Input: `"hello"`
Conclusion: `"How can I help you?"`

2. The `"add [name] [phone number]"` command. For this command, let's make the `add_contact` function:

Input: `"add John 1234567890"`
Output: `"Contact added."`

3. The `"change [name] [new phone number]"` command. For this command, let's make the `change_contact` function:

Input: `"change John 0987654321"`
Output: `"Contact updated."` or an error message if the name is not found

4. The `"phone [name]"` command. For this command, let's make the `show_phone` function:

Input: `"phone John"`
Output: `[phone number]` or an error message if the name is not found

5. The `"all"` command. For this command, let's make the `show_all` function:

Input: `"all"`
Output: all saved contacts with phone numbers

6. `"close"` or `"exit"` command. Since the execution of the program must be interrupted here, you can do without the function for these commands for now:

Input: any of these words
Output: `"Good bye!"` and ending the bot

Any command that does not conform to the above formats will be considered invalid by us, and the bot will display the message `"Invalid command."`

Let's start with a simple version of the CLI bot:

```python
def main():
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
```

When the program starts, it displays the message `"Welcome to the assistant bot!"` and enters an infinite loop where it waits for a command input from the user `while True`.

If the user types `"close"` or `"exit"`, the program outputs `"Good bye!"` and completes the work. The code block is responsible for this:

```python
if command in ["close", "exit"]:
    print("Good bye!")
    break
```

If the user types `"hello"`, the program outputs `"How can I help you?"`. If the entered command does not correspond to any of these options, the program displays `"Invalid command."`.

```python
Welcome to the assistant bot!
Enter a command: test
Invalid command.
Enter a command: hello
How can I help you?
Enter a command: exit
Good bye!
```

This code creates a simple interactive command prompt that responds to a limited set of commands. We've implemented a request-response loop that will serve as a great foundation for adding functionality in future homework assignments.

Now let's add a command parser. Let's rewrite our code as follows

```python
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
```

We've added a `parse_input(user_input)` function that takes the user input string `user_input` and splits it into words using the `split()` method. It returns the first word as the command `cmd` and the rest as a list of arguments `*args`. A line of `cmd` code, `*args = user_input.split()` splits a string into words. The first word is stored in the `cmd` variable and the rest is stored in the `args` list thanks to the \* unpacking operator. Next, the line of code `cmd = cmd.strip().lower()` removes extra spaces around the command and converts it to lower case.

#### ☝Why lowercase the command?

Suppose a user enters a command like `"HELLO"`, `"Hello"` or `"hello"`. If you don't bring these options to a common case, they will be treated as different commands and you will have to handle each option separately.

> [!IMPORTANT] Lowercase the command avoids this by converting all options to the same form. This way, you can easily compare an entered command with predefined commands, regardless of how the user entered it. This provides a better user experience as the application becomes less sensitive to the specific way commands are entered.

We will get the result in the main function after executing the line of code `command, \*args = parse_input(user_input)`.

The `parse_input` function splits the input string into words, using a space as the delimiter. The `command` variable takes the first value and is considered a command, and the `args` variable becomes a list of all other values.

For example, if we enter the command `"add John 123456"` then the `command` variable will become the string `"add"` and the `args` variable will become the list `["John", "123456"]` . If we enter the command `"hello"`, command will be the string `"hello"`, and `args` will be an empty list `[]`

Hopefully, you have now understood the principle of the parser, it's time to add the `add` command.

```python
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
```

We added a contact dictionary `contacts = {}` in the middle of the `main` function and the handler function of the `add_contact` command.

The `add_contact` function is designed to add a new contact to the contact dictionary. It takes two arguments: `args`, which is a list containing the name and phone number, and `contacts`, which is a dictionary where the contacts are stored.

Inside the function, the two items from the `args` list are unpacked into the `name` and `phone` variables. The function then adds a key:value pair to the contacts dictionary using the name as the key and the phone number as the value `contacts[name] = phone`.

> [!IMPORTANT] ☝ It should be noted that if a contact with such a name already exists, its data will be overwritten without any warnings. Here you can already act at your discretion, whether you want to process the collision or not, in our version we overwrite the contact.

The `add_contact` function returns a string confirming the successful addition of a contact: `"Contact added."`.

It should be noted that this function does not have built-in checks for input errors. For example, if `args` does not contain two elements, this function will throw a `ValueError`.

```python
ValueError: not enough values to unpack (expected 2, got 0)
```

Leave the error handling in this homework up to you, because in the next homework we will add error handling through decorators.

#### Evaluation criteria:

- The bot should be in an infinite loop waiting for a user command.
- The bot completes its work if it encounters the words: `"close"` or `"exit"`.
- The bot is not case sensitive.
- The bot accepts commands:
- `"hello"`, and responds to the console with the message `"How can I help you?"`
- `"add username phone"`. With this command, the bot saves a new contact in memory, for example in a dictionary. The user enters the name `username` and the phone number phone, necessarily with a space.
- `"change username phone"`. With this command, the bot stores in memory the new telephone number `phone` for the `username` contact, which already exists in the notebook.
- `"phone username"` With this command, the bot displays the phone number for the specified `username` contact in the console.
- `"all"`. With this command, the bot outputs all saved contacts with phone numbers to the console.
- `"close"`, `"exit"` according to any of these commands, the bot ends its work after outputting the message `"Good bye!"` to the console. and will complete its execution.
- Command logic is implemented in separate functions, and these functions accept one or more strings as input and return a string.
  All the logic of interaction with the user is implemented in the `main` function, all `print` and `input` occur only there.
