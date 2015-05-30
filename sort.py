"""Sorts the datas in ascending order or descending order"""

from tree import tree

class sort:
    def __init__(self, args):
        #construct sort tree
        sort_d = self.sort_dsc
        sort_a = self.sort_asc
        self.args = args
        self.tree = tree('sort')
        self.tree.addchild('-d')
        self.tree.addchild('-a')
        self.tree.addchild('--ascending')
        self.tree.addchild('--descending')
        self.tree.getchild('-d').addchild(sort_d)
        self.tree.getchild('--descending').addchild(sort_d)
        self.tree.getchild('--ascending').addchild(sort_a)
        self.tree.getchild('-a').addchild(sort_a)

    def parse(self):
        height = 1
        temp = self.tree
        #to check if the command is correct
        while height != 2:
            temp = self.tree.getchild(self.args[height])
            height += 1


        if temp == False:
            print("command not found")
            return
        x = temp.getallvalues()
        return x[0].getroot()(self.args[-1])


    def sort_asc(self,file_name):
        fi = open(file_name)
        x = fi.read()
        answer = x.split(' ')
        answer.sort()
        return ' '.join(answer)
         
    def sort_dsc(self, file_name):
        fi = open(file_name)
        x = fi.read()
        answer = x.split(' ')
        answer.sort(reverse=True)
        return ' '.join(answer)
