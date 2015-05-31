"""Module to read files"""

class cat:
    def __init__(self, expr):
        self.args = expr

    def parse(self):
        if self.args[1]:
            self.read(self.args[1])
        else:
            print('invalid command')

    def read(self, file_name):
        fi = open(file_name, 'r')
        print(fi.read())
        
