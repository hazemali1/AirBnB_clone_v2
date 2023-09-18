# 0x00. AirBnB Clone - The Console

![AirBnB Clone Logo](https://camo.githubusercontent.com/59589bd21e8ec09ef94f2d9bb80d36d144bc487fe4737f8b213d005f3273921b/68747470733a2f2f696d6775722e636f6d2f4f696c457358562e706e67)

This is the README file for the **0x00. AirBnB Clone - The Console** project. This project is part of the Holberton School curriculum and aims to create a simple command-line interface (CLI) for managing and interacting with objects in a clone of the Airbnb website.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Command Examples](#command-examples)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)

## Description

The **0x00. AirBnB Clone - The Console** project is a command-line tool that simulates the basic functionalities of the Airbnb website. It allows users to interact with and manage various objects, such as User, Place, State, City, Amenity, and Review, through a command-line interface.

The console supports various commands that enable users to create, update, delete, and display objects. It also offers features like searching for objects, displaying statistics, and saving/loading data to/from JSON files.

## Features

- Interactive command-line interface.
- Create, read, update, and delete objects (User, Place, State, City, Amenity, Review).
- Search and display objects based on various criteria.
- Display statistics about the number of created objects.
- Save objects to a JSON file and load objects from a JSON file.

## Installation

1. Clone this repository to your local machine using:
```
git clone https://github.com/Omartalat/AirBnB_clone.git
```

2. Navigate to the project directory:
```
cd airbnb_clone
```
3. Run the console:
```
./console.py
```

## Usage

1. Run the console by executing `./console.py`.

2. You will enter the interactive command-line interface.

3. Use various commands to interact with objects and manage the Airbnb clone.

## Command Examples

Here are some examples of commands you can use in the console:

- `help`: Display available commands and their usage.
- `create <class_name>`: Create a new object of the specified class.
- `show <class_name> <object_id>`: Display information about a specific object.
- `all`: Display information about all objects.
- `update <class_name> <object_id> <attribute_name> "<attribute_value>"`: Update an object's attribute.
- `destroy <class_name> <object_id>`: Delete an object.
- `quit`: Exit the console.

For detailed information on commands and their usage, refer to the built-in help command within the console.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or a pull request in the GitHub repository.

## Authors

This project is developed by students of Holberton School.

- @Omartalat
- @hazemali1

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
