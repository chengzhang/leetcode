from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        layer = [root]
        direction = 1
        while layer:
            nxt = []
            val = []
            for node in layer:
                if node:
                    val.append(node.val)
                    nxt.append(node.left)
                    nxt.append(node.right)
            if val:
                res.append(val[::direction])
            layer = nxt
            direction *= -1
        return res

