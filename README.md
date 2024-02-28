# Holberton's AIRBnB Clone

## Overview
The Holberton AIRBnB Clone project is the initial step in constructing a web application that emulates AirBnB's functionality. This phase is crucial as it lays the groundwork for subsequent projects, including HTML/CSS templating, database storage, API development, and front-end integration.

## The HBNB Console
---
The HBNB Console resembles the Shell but is tailored for a specific use-case. Its purpose is to manage the objects within our project efficiently, allowing users to perform tasks such as creating, retrieving, updating, and deleting objects.

## Commands and Usage
The command interpreter facilitates data management with the following commands:

| Command | Function |
| ------- | -------- |
| create | Creates a new instance of a class |
| show | Displays the information of an instance of a class |
| destroy | Deletes an instance of a class |
| update | Modifies the information of the objects in an instance |
| all | Displays information of all instances in an instance |
| quit | Exits the console |
| help | Displays help for the commands |

## Object Types
The console supports various object types, including:

| Object | Description |
| ------ | ----------- |
| city | City of the reservation |
| state | Country state of the reservation |
| place | Name of the place of reservation |
| user | Name of the user who reserves |
| amenity | Amenities of the place |
| review | Reviews of the room and the guest |

### Getting Started with the Console
To initiate the console, execute the command:
```./console```

You'll see:
```(hbnb)```

Now, you can begin using the HBNB console.

## Using the HBNB Console
### Syntax:
``` <command> <classname> <id>```

Note: ID doesn't apply to the create command.

### For Help:
```help <command>```

### Examples:
#### For Help:

(hbnb)help create
create a new instace of a class
(hbnb)

#### For standard commands:

(hbnb)create User
993e570d-9b4e-449c-84b3-085ab454d3ce
(hbnb)

Create a new User

(hbnb)create BaseModel
d711be23-73d9-4fbd-92f5-fe9ec7044d6d
(hbnb)show BaseModel d711be23-73d9-4fbd-92f5-fe9ec7044d6d
[BaseModel] (d711be23-73d9-4fbd-92f5-fe9ec7044d6d) {'id': 'd711be23-73d9-4fbd-92f5-fe9ec7044d6d', 'created_at': '2019-07-04T02:20:53.149558', 'updated_at': '2019-07-04T02:20:53.149791'}
(hbnb)

Create a new BaseModel and show the objects of the instance.

(hbnb)destroy BaseModel d711be23-73d9-4fbd-92f5-fe9ec7044d6d
['BaseModel', 'd711be23-73d9-4fbd-92f5-fe9ec7044d6d']
(hbnb)

Pretty self explanatory. Destroy the objects.


