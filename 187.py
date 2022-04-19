# coding = utf8

"""
前缀树（Trie）
"""

from typing import List


class TrieNode(object):
    def __init__(self, value=''):
        self.value = value
        self.children = {}
        self.cnt = 0

    def add_path(self, path):
        node = self
        for char in path:
            if char not in node.children:
                child = TrieNode(char)
                node.children[char] = child
            node = node.children[char]
        node.cnt += 1

    def repeat_path(self):
        res = []
        prefix = []

        def __dfs(node):
            prefix.append(node.value)
            if node.cnt > 1:
                res.append(''.join(prefix))
            for child in node.children.values():
                __dfs(child)
            prefix.pop()

        __dfs(self)
        return res


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        trie = TrieNode()
        N = len(s)
        for i in range(0, N-9):
            path = s[i:i+10]
            trie.add_path(path)
        return trie.repeat_path()


if __name__ == '__main__':
    cases = [
        ("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["AAAAACCCCC","CCCCCAAAAA"]),
        ("AAAAAAAAAAAAA", ["AAAAAAAAAA"]),
    ]
    sln = Solution()
    for case in cases:
        s, golden = case
        res = sln.findRepeatedDnaSequences(s)
        print(golden, res)
