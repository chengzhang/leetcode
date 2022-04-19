from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = [1]
        res = [root.val]

        def _dfs(node):
            if not node:
                return False
            if _dfs(node.left):
                return True
            if order[0] == k:
                res[0] = node.val
                return True
            order[0] += 1
            if _dfs(node.right):
                return True
            return False

        _dfs(root)
        return res[0]
