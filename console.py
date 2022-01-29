#!/usr/bin/python3

"""
module Console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand
       Attributes:
           prompt (str): prompt
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        return True

    def emptyline(self):
        """an empty line do nothing"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
