"""Module that lists out all the directory and files of the system
   Could be used to search for particular files, for example all the
   mp3 files.
"""

import os
from tree import tree

class folder:

    def __init__(self):
        self.location = os.getcwd()

    def _getdirs(self, tree, dir_list):
        #recursive functin is used to acheive the ability to backtrack with ease.

        temp = [os.path.join(tree.getroot(), f) for f in os.listdir(tree.getroot()) if not os.path.isfile(os.path.join(tree.getroot(), f))]
        for x in temp:
            tree.addchild(x)
            dir_list.append(x)
            self._getdirs(tree.getchild(x), dir_list)

        else:
            return dir_list


    def getdirs(self, search):
        try:
            if search:
                return self._getdirs(tree(search), [])

            return [x for x in os.listdir(self.location) if not os.path.isfile(os.path.join(self.location, x))]

        except:
            print("Invalid directory")
            return
