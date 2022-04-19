# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            lres, lsum = dfs(node.left)
            rres, rsum = dfs(node.right)
            res = abs(lsum - rsum) + lres + rres
            s = lsum + rsum + node.val
            return res, s
        return dfs(root)[0]
