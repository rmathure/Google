__author__ = 'rohanmathure'


class Tree:
    def __init__(self):
        self.__root = None

    def setRoot(self, node):
        self.__root = node

    def getRoot(self):
        return self.__root