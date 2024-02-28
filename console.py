#!/usr/bin/python3

import cmd
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import ClassList


class HBNBCommand(cmd.Cmd):
    """This is the console for the AirBnB project"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing if an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel and prints the id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        tokens = arg.split()

        try:
            new_instance = eval(tokens[0])()
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance"""
        token = args.split()

        if len(token) == 0:
            print("** class name missing **")
            return
        if len(token) == 1:
            print("** instance id missing **")
            return
        try:
            eval(token[0])
        except Exception:
            print("** class doesn't exist **")

        objDict = storage.all()
        keyId = token[0] + "." + token[1]

        try:
            value = objDict[keyId]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name"""
        token = args.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        if token[1] == 0:
            print("** instance id missing **")

        try:
            eval(token[0])
        except Exception:
            print("** class doesn't exist **")
        objDict = storage.all()
        keyId = token[0] + "." + token[1]

        try:
            del objDict[keyId]
        except Exception:
            print("** no instance found **")
        storage.save()

    def do_all(self, arg):
        """ Prints string represention of all instances of a given class """

        if not arg:
            print("** class name missing **")
            return

        token = arg.split()

        if token[0] not in ClassList:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            newList = []

            for key, val in all_objs.items():
                ob_name = val.__class__.__name__
                if ob_name == token[0]:
                    newList += [val.__str__()]
            print(newList)

    def do_update(self, args):
        """ Updates an instance based on the class name and id """

        if not args:
            print("** class name missing **")
            return

        token = args.split()

        if token[0] not in ClassList:
            print("** class doesn't exist **")
        elif len(token) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, val in all_objs.items():
                ob_name = val.__class__.__name__
                ob_id = val.id
                if ob_name == token[0] and ob_id == token[1].strip('"'):
                    if len(token) == 2:
                        print("** attribute name missing **")
                    elif len(token) == 3:
                        print("** value missing **")
                    else:
                        setattr(val, token[2], token[3])
                        storage.save()
                    return
            print("** no instance found **")


if __name__ == "__main__":
    console = HBNBCommand()
    console.cmdloop()
