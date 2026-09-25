# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def DFS(self,root):
            if not root:
                return
            if not self.ans:
                return
            self.DFS(root.left)
            if self.cur_max>=root.val:
                self.ans = False
                return
            self.cur_max = root.val
            self.DFS(root.right)
            return
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.cur_max = float('-inf')
        self.DFS(root)
        return self.ans