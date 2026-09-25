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
            if self.cnt>=self.k:
                return
            self.DFS(root.left)
            self.cnt+=1
            if self.cnt == self.k:
                self.ans = root.val
            self.DFS(root.right)
            return
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.cnt = 0
        self.ans = None
        self.DFS(root)
        return self.ans