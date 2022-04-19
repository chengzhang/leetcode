# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        res = 0
        layer, nxt = [root], []
        while layer:
            nxt.clear()
            for node in layer:
                if node and node.children:
                    for c in node.children:
                        nxt.append(c)
            if nxt:
                res += 1
            layer, nxt = nxt, layer
        return res

