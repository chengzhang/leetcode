class Node(object):
    def __init__(self, c=''):
        self.sum = 0
        self.c = c
        self.end = False
        self.value = 0
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = Node()

    def add(self, key, value):
        node = self.root
        stack = [node]
        for i, k in enumerate(key):
            if k not in node.children:
                node.children[k] = Node(k)
            node = node.children[k]
            stack.append(node)
        if node.end:
            delta = value - node.value
        else:
            delta = value
            node.end = True
        for n in stack:
            n.sum += delta

    def get_sum(self, prefix):
        node = self.root
        for i, k in enumerate(prefix):
            if k not in node.children:
                return 0
            node = node.children[k]
        return node.sum


class MapSum:

    def __init__(self):
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.add(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.get_sum(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)