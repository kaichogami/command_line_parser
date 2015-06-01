"""Search for particular extension files in given directory"""

class list_all:

    def __init__(self, args):
        self.args = args
        self.length = len(self.args)


    def parse(self):

        if self.length == 3:
            return self.list_folders(self.args[-1])

        elif self.length == 4:
            return self.list_files(self.args[-2], self.args[-1])

        else:
            return "invalid command arguements"


    def list_files(self, extension, path = '/media'):
        from file import files

        length = len(extension)
        obj = files()
        temp = obj.show(path = path)

        if extension == 'all':
            return '\t'.join(temp)

        else:
            result = [x for x in temp if x[-length:]==extension]
            return '\t'.join(result)


    def list_folders(self, path = '/media'):
        from folder import folder

        obj = folder()
        result = obj.getdirs(search = path)
        return '\t'.join(result)
