# AirBnB Clone

This project is a simple command-line application inspired by AirBnB.

The project allows us to create, display, update, and delete objects.

## Command Interpreter

The command interpreter will allow users to interact with AirBnB objects
from the command line.

### How to start the console

Run:

    ./console.py

The console will display:

    (hbnb)

### How to use it

Commands can be entered after the `(hbnb)` prompt.

Examples:

    (hbnb) help
    (hbnb) quit

### Common commands

| Command | What it does |
| --- | --- |
| `create <ClassName>` | Create an object and print its ID. |
| `all [ClassName]` | List all objects, or only objects of the selected class. |
| `show <ClassName> <id>` | Display one object by its ID. |
| `update <ClassName> <id> <attribute> <value>` | Set an object's attribute to a value. |
| `destroy <ClassName> <id>` | Delete an object by its ID. |
| `quit` | Exit the console. |

For example, create a user, copy the ID printed by the console, and use it
in the commands that follow:

    (hbnb) create User
    (hbnb) all User
    (hbnb) show User <id>
    (hbnb) update User <id> first_name Vanessa
    (hbnb) destroy User <id>

Replace `<id>` with the ID returned by `create`. The commands that use a
class name accept `BaseModel`, `User`, `State`, `City`, `Amenity`,
`Place`, or `Review`.

### Project goals

The project teaches:

- Python packages
- Object-oriented programming
- Serialization and deserialization
- JSON file storage
- UUIDs
- datetime
- Unit testing
- Command interpreters

## MySQL Storage

This version of the AirBnB clone extends the project to support MySQL database storage using SQLAlchemy.

The application can switch between file storage and database storage using environment variables without changing the application logic.

### Team

- Joseph Albert
- Vanessa Kittivo
