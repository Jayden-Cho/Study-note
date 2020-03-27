class TreeNode:
    nodeLHS = None
    nodeRHS = None
    nodeParent = None
    value = None

    def __init__(self, value, nodeParent):
        self.value = value
        self.nodeParent = nodeParent

    def getLHS(self):
        return self.nodeLHS
    def getRHS(self):
        return self.nodeRHS
    def getValue(self):
        return self.value
    def getParent(self):
        return self.nodeParent
    def setLHS(self, LHS):
        self.nodeLHS = LHS
    def setRHS(self, RHS):
        self.nodeRHS = RHS
    def setVaue(self, value):
        self.value = value
    def setParent(self, nodeParent):
        self.nodeParent = nodeParent

class BinarySearchTree:
    root None

    def __init__(self):
        pass

    def insert(self, value, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            self.root = TreeNode(value, None)
            return
        if value == node.getValue():
            return
        if value > node.getValue():
            if node.getRHS() is None:
                node.setRHS(TreeNode(value, node))
            else:
                self.insert(value, node.getRHS())
        if value < node.getValue():
            if node.getLHS() is None:
                node.setLHS(TreeNode(value, node))
            else:
                self.insert(value, node.getLHS())
        return

    def search(self, value, node=None):
        if node is None:
            node = self.root
        if value == node.getValue():
            return True
        if value > node.getValue():
            if node.getRHS() is None:
                return False
            else:
                return self.search(value, node.getRHS())
        if value < node.getValue():
            if node.getLHS() is None:
                return False
            else:
                return self.search(value, node.getLHS())

    def delete(self, value, node=None):
        if node is None:
            node = self.root
        if node.getValue() < value:
            return self.delete(value, node.getRHS())
        if node.getValue() > value:
            return self.delete(value, node.getLHS())
        if node.getValue() == value:
            if node.getLHS() is not None and node.getRHS() is not None:
                nodeMin = self.findMin(node.getRHS())
                node.setValue(nodeMin.getValue())
                self.delete(nodeMin.getValue(), node.getRHS())
                return
            parent = node.getParent()
            if node.getLHS() is not None:
                if node == self.root:
                    self.root = node.getLHS()
                elif parent.getLHS() == node:
                    parent.setLHS(node.getLHS())
                    node.getLHS().setParent(parent)
                else:
                    parent.setRHS(node.getLHS())
                    node.getLHS().setParent(parent)
                return
            if node.getRHS() is not None:
                if node == self.root:
                    self.root = node.getRHS()
                elif parent.getLHS() == node:
                    parent.setLHS(node.getRHS())
                    node.getRHS().setParent(parent)
                else:
                    parent.setRHS(node.getLHS())
                    node.getLHS().setParent(parent)
                return
            if node.getRHS() is not None:
                if node == self.root:
                    self.root = node.getRHS()
                elif parent.getLHS() == node:
                    parent.setLHS(node.getRHS())
                    node.getRHS().setParent(parent)
                else:
                    parent.setRHS(node.getRHS())
                    node.getRHS().setParent(parent)
                return
            if node == self.root:
                self.root = None
            elif parent.getLHS() == node:
                parent.setLHS(None)
            else:
                parent.setRHS(None)
            return

    def findMax(self, node):