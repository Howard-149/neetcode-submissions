# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            if not p and not q:
                return True
            else:
                return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.ans = False
        self.stack = [root]
        while self.stack and not self.ans:
            cur = self.stack.pop()
            if cur:
                if cur.val == subRoot.val:
                    self.ans = self.isSameTree(cur,subRoot)
                self.stack.append(cur.left)
                self.stack.append(cur.right)
        return self.ans
