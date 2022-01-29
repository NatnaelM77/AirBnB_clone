#!/usr/bin/python3

"""
module Console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand"""
    prompt = '(hbnb) '

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        """init method"""
        super().__init__(completekey, stdin, stdout)

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
