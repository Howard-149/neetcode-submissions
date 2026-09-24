# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def Height(self,root) -> int:
            if not root:
                return 0
            l = self.Height(root.left)
            r = self.Height(root.right)
            self.ans = max(self.ans,l+r)
            return max(l,r)+1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        if not root:
            return 0
        self.Height(root)
        return self.ans
