def traverseLevelOrder(self):
    ret = []
    Q = Queue()
    Q.enqueue(self.root)
    while not Q.isEmpty():
        node = Q.dequeue()
        if node is None:
            continue
        ret.append(node.getValue())
        if node.getLHS() is not None:
            Q.enqueue(node.getLHS())
        if node.getRHS() is not None:
            Q.enqueue(node.getRHS())
    return ret