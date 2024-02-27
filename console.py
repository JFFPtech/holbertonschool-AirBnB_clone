#!/usr/bin/python3
"""This is the console for the AirBnB project"""

import cmd

class HBNBCommand(cmd.Cmd):
    """This is the console for the AirBnB project"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing if an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()