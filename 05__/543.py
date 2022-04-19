# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            l_dep, l_res = dfs(node.left)
            r_dep, r_res = dfs(node.right)
            return max(l_dep, r_dep) + 1, max(l_dep + r_dep + 1, l_res, r_res)
        return dfs(root)[1]

