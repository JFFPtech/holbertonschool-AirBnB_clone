# holbertonschool-AirBnB_clone
# 0x00. AirBnB clone - The console
### `Group project` `Python` `OOP`

![65f4a1dd9c51265f49d0](https://github.com/samuelselasi/AirBnB_clone/assets/85158665/a3c085f0-cd74-4e8e-a4a9-6d07e6880c38)

## Background Context
Welcome to the **AirBnB** clone project!

The aim of the project is to deploy on one's own server
a simple copy of the [AirBnB website](https://www.airbnb.com/).

## Resources
**Read or watch**:

* [cmd module](https://docs.python.org/3.8/library/cmd.html)
* [cmd module in depth](http://pymotw.com/2/cmd/)
* **packages concept page**
* [uuid module](https://docs.python.org/3.8/library/uuid.html)
* [datetime](https://docs.python.org/3.8/library/datetime.html)
* [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
* [cmd module wiki page](https://wiki.python.org/moin/CmdModule)
* [python unittest](https://realpython.com/python-testing/)

## General
# Command Line Interpreter for Airbnb Clone - The Console
This command line interpreter is designed for an Airbnb clone application. It allows users to interact with the application's backend through a console, where they can create and manage instances of the application's classes.

## How to Use
To start the console, run the script `console.py`. This will start the command line interpreter, and the prompt `(hbnb)` will be displayed. This prompt indicates that the console is ready to accept user input.

The following commands are available:

* `create`: Creates a new instance of a class.
* `show`: Prints the string representation of an instance.
* `destroy`: Deletes an instance based on the class name and ID.
* `all`: Prints all string representations of all instances, or all instances of a particular class.
* `update`: Updates an instance based on the class name and ID.
* `count`: Counts the instances of a class.
* `EOF`: Exits the console.
* `quit`: Exits the console.

The syntax for each command is as follows:

* `create <class name>`: Creates a new instance of the specified class.
* `show <class name> <instance id>`: Prints the string representation of the specified instance.
* `destroy <class name> <instance id>`: Deletes the specified instance.
* `all`: Prints the string representations of all instances.
* `all <class name>`: Prints the string representations of all instances of the specified class.
* `update <class name> <instance id> <attribute name> "<attribute value>"`: Updates the specified instance with the specified attribute value.
* `count <class name>`: Counts the instances of the specified class.

## Requirements
### Python Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version `2.8.*`)
* All your files must be executable
* The length of your files will be tested using `wc`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests
* Allowed editors: `vi`, `vim`, `emacs`
* All your files should end with a new line
* All your test files should be inside a folder [tests](./tests)
* You have to use the [unittest](https://docs.python.org/3.4/library/unittest.html#module-unittest) module
* All your test files should be python files (extension: `.py`)
* All your test files and folders should start by `test_`
* Your file organization in the tests folder should be the same as your project
* e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
* e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
*  All your tests should be executed by using this command: `python3 -m unittest discover tests`
* You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

## More Info
### Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`

![815046647d23428a14ca](https://github.com/samuelselasi/AirBnB_clone/assets/85158665/c57fe779-0bd5-4be1-b0eb-5280fe97fd55)