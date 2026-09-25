# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isGood(self,root,cur_max):
        if not root:
            return
        if root.val>=cur_max:
            self.ans+=1
            cur_max = root.val
        self.isGood(root.left,cur_max)
        self.isGood(root.right,cur_max)
        return
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 1
        self.isGood(root.left,root.val)
        self.isGood(root.right,root.val)
        return self.ans