"""Search for particular extension files in given directory"""

class search:

    def __init__(self, args)
        #construct search tree to parse
        self.tree = tree('search')
        self.tree.addchild(['-f', '--files'])
        self.tree.addchild(['-d', '--directories'])
        self.tree.getchild('-f').addchild()
        self.tree


    def search_file(self, file_name, whole = False, path'/media'):
        from files import files

        obj = files()
        temp = obj.show(whole = whole, path = path)

        result = [x for x in temp if x == file_name]
        return '\t'.join(result)


    def list_files(self, extension, whole = False, path = '/media'):
        from files import files

        length = len(extension)
        obj = files()
        temp = obj.show(whole = whole, path = path)

        result = [x for x in temp if x[-length:]==extension]
        return '\t'.join(result)


    def list_folders(self, whole = False, path = '/media'):
        from folder import folder

        obj = folder()
        result = obj.getdirs(whole=whole, search = path)
        return '\t'.join(result)
