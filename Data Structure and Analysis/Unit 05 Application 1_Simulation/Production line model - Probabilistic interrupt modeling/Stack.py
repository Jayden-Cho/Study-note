from ProductionList import ProductionList


class Stack(ProductionList):
    def __init__(self):
        self.List = ProductionList('')

    def add(self, Object):
        self.List.addFirst(Object)

    def get(self):
        Object = self.List.removeFirst()
        return Object

    def getSize(self):
        size = self.List.getSize()
        return size

    def getListString(self):
        string = self.List.getListString()
        return string