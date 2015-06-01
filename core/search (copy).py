"""Search for particular file in given directory"""
from tree import tree

class search:

    def __init__(self, args):
        #construct search tree to parse
        self.args = args
        self.length = len(args)

        if self.length == 3:
            print(self.args)
            self.tree = tree('search')
            self.tree.addchild(self.args[1])
            self.tree.getchild(self.args[1]).addchild(self.args[2])
            self.tree.getchild(self.args[1]).getchild(self.args[2]).addchild(self.search_file)


    def search_file(self, file_name, path):
        from files import files

        obj = files()
        temp = obj.show(path = path)

        result = [x for x in temp if x == file_name]
        return '\t'.join(result)


    def parse(self):
        height = 1
        if self.length != 3:
            return "invalid command length"
        temp = self.tree

        #to check if command is right and to point to right function
        while height != 3:
            temp = self.tree.getchild(self.args[height])
            height += 1

        x = temp.getallvalues()
        print(x[0].getroot())
        return x[0].getroot()(self.args[-2], self.args[-3])

