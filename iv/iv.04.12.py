# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        values = []
        res = [0]

        def __dfs(node):
            if not node:
                return
            for i in range(len(values)):
                values[i] += node.val
            values.append(node.val)
            for i in range(len(values)):
                if values[i] == sum:
                    res[0] += 1
            __dfs(node.left)
            __dfs(node.right)
            values.pop()
            for i in range(len(values)):
                values[i] -= node.val

        __dfs(root)
        return res[0]
