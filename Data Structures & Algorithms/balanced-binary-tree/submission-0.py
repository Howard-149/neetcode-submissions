# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def Height(self,root):
        if not root:
            return 0
        if not self.bal:
            return 0
        l = self.Height(root.left)
        r = self.Height(root.right)
        if abs(l-r) > 1:
            self.bal = False
        return 1 + max(l,r)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True
        self.Height(root)
        return self.bal