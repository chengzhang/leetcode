# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return root if not root or root.val == val else root.val < val and self.searchBST(root.right, val) or self.searchBST(root.left, val)

    def searchBST1(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
        return root.val < val and self.searchBST(root.right, val) or self.searchBST(root.left, val)

    def searchBST2(self, root: TreeNode, val: int) -> TreeNode:
        while root and root.val != val:
            root = root.val < val and root.right or root.left
        return root

