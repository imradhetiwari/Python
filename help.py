#
help(print)

#A class with functions
class Helper:
    def __init__(self):
        '''The helper class is intialized'''

    def print_help(self):
        '''Returns the help description'''
        print("helper description")

help(Helper)
help(Helper.print_help)