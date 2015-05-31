"""Base tree class for parsing arguments"""

class tree:
    def __init__(self, value):
        self.root = value
        self.child_count = 1
        self.children = {}

    def addchild(self, value):
        for x in value:
            child = tree(x)
            self.children[x] = child

    def setroot(self, value):
        self.root = value

    def getroot(self):
        return self.root

    def getchild(self, value):
        try:
            if self.children[value]:
                return self.children[value]

        except:
            return False

    def getallvalues(self):
        return self.children.values()



