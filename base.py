"""Base class for command line interface. It acts as the brain. It compares
   the first argument of the command and matches it with the given COMMANDS.
   Then it calls the respective class to do the work.
"""
import sys

COMMANDS = ['cat', 'sort', 'search', 'list']

class base:
    def __init__(self, expr):
        self.expr = expr.split(' ')

    def check_command(self):
        if self.expr[0] in COMMANDS:
            return True

        else:
            return False

    def do(self):
         if self.check_command() == False:
            print ('Command not found')
            return '\n'

         if self.expr[0] == 'sort':
            from core.sort import sort
            action = sort(self.expr)
            print(action.parse())

         elif self.expr[0] == 'cat':
            from core.cat import cat
            action = cat(self.expr)
            print(action.parse())

         elif self.expr[0] == 'search':
            from core.search import search
            action = search(self.expr)
            print(action.parse())

         elif self.expr[0] == 'list':
            from core.listall import list_all
            action = list_all(self.expr)
            print(action.parse())
            
