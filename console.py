#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """This is the console for the AirBnB project"""
    prompt = '(hbnb) '

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
        if not arg:
            print("** class name missing **")
            return
        try:
            cls_name = arg.split()[0]
            if cls_name in globals():
                new_instance = eval(arg)()
                print(new_instance.id)
                new_instance.save()
            else:
                print("** class doesn't exist **")
        except IndexError:
            print("** class name missing **")
        

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        if not arg:
            print("** instance id missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        cls_name = args[0]
        obj_id = args[1]
        key = "{}.{}".format(cls_name, obj_id)
        try:
            with open("file.json", "r") as file:
                try:
                    data = json.load(file)
                    if key in data:
                        print(data[key])
                    else:
                        print("** no instance found **")
                except json.JSONDecodeError:
                    print("** JSON file is empty or invalid **")
        except FileNotFoundError:
            print("** JSON file not found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            cls_name = args[0]
            obj_id = args[1]
            key = "{}.{}".format(cls_name, args[1])
            try:
                with open("file.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = {}
            if key in data:
                del data[key]
                with open("file.json", "w") as file:
                    json.dump(data, file)
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        try:
            with open("file.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        except json.JSONDecodeError:
            print("** JSON file is empty or invalid **")
            return
        
        if not arg:
            print([str(v) for v in data.values()])
        else:
            try:
                cls_name = arg.split()[0]
                print([str(v) for k, v in data.items() if cls_name in k])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(cls_name, args[1])
            try:
                with open("file.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = {}
            if key in data:
                obj_dict = data[key]
                if cls_name in globals():
                    # Create an instance of the class associated with the object
                    obj_instance = globals()[cls_name](**obj_dict)
                    if len(args) < 3:
                        print("** attribute name missing **")
                        return
                    if len(args) < 4:
                        print("** value missing **")
                        return
                    obj_dict[args[2]] = args[3].strip('"')
                    obj_instance.save()  # Save the updated instance
                    with open("file.json", "w") as file:
                        json.dump(data, file)
                else:
                    print("** class doesn't exist **")
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()