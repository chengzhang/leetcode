# coding = utf8

from typing import List
from collections import defaultdict
import pdb


"""
并查集
"""


class TreeNode(object):
    def __init__(self, name):
        self.name = name
        self.hash = hash(self.name)
        self.cnt = 1
        self.unique_name = name

    def __hash__(self):
        return self.hash


class UnionFindTree(object):
    def __init__(self, synonym_pairs):
        self.parent = {}
        self.nodes = {}
        self._build(synonym_pairs)

    def _build(self, synonym_pairs):
        for a, b in synonym_pairs:
            a_node = self._find(a)
            b_node = self._find(b)
            self._union(a_node, b_node)

    def unique_name(self, name):
        if name in self.nodes:
            root = self._find_root(self.nodes[name])
            return root.unique_name
        return name

    def _find(self, name):
        if name in self.nodes:
            node = self.nodes[name]
        else:
            node = TreeNode(name)
            self.nodes[name] = node
        return node

    def _find_root(self, node):
        ori = node
        while node in self.parent:
            node = self.parent[node]
        if ori != node:
            self.parent[ori] = node
        return node

    def _union(self, a: TreeNode, b: TreeNode):
        ar = self._find_root(a)
        br = self._find_root(b)
        if ar != br:
            if ar.cnt < br.cnt:
                ar, br = br, ar
            self.parent[br] = ar
            ar.cnt += br.cnt
            ar.unique_name = min(ar.unique_name, br.unique_name)


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        synonym_pairs = []
        for i in synonyms:
            i = i[1:-1]
            a, b = i.split(',')
            synonym_pairs.append([a, b])
        tree = UnionFindTree(synonym_pairs)
        summary = defaultdict(int)
        for i in names:
            name, freq = i[:-1].split('(')
            freq = int(freq)
            name = tree.unique_name(name)
            summary[name] += freq
        res = []
        for name, freq in summary.items():
            res.append(f'{name}({freq})')
        return res


if __name__ == '__main__':
    cases = [
        (["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"], ["John(27)","Chris(36)"]),
    ]
    sln = Solution()
    for case in cases:
        names, synonyms, golden = case
        res = sln.trulyMostPopular(names, synonyms)
        print(golden, res)
