# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level_nodes = defaultdict(int)
        queue = deque([(root,0)])
        ans = []
        while queue:
            node,level = queue.popleft()
            if node:
                queue.append((node.right,level+1))
                queue.append((node.left,level+1))
                if not level_nodes[level]:
                    level_nodes[level]= node.val
        for i in range(level):
            ans.append(level_nodes[i])
        return ans