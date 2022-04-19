class Node(object):
    def __init__(self, c):
        self.char = c
        self.end = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = Node('')

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                son = Node(c)
                node.children[c] = son
                node = son
            else:
                node = node.children[c]
        node.end = True

    def search(self, word: str) -> bool:
        def __dfs(node, i):
            if i == len(word):
                return node.end
            if word[i] == '.':
                for c, son in node.children.items():
                    if __dfs(son, i+1):
                        return True
                return False
            c = word[i]
            if c not in node.children:
                return False
            node = node.children[c]
            return __dfs(node, i+1)

        return __dfs(self.root, 0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)