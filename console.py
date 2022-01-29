#!/usr/bin/python3

"""
module Console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand
    Attributes:
        prompt (str): The command prompt.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit console"""
        return True

    def emptyline(self):
        """emptyline. Do nothing"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
