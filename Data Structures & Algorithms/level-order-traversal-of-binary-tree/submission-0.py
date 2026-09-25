# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_nodes = defaultdict(list)
        queue = deque([(root,0)])
        ans = []
        while queue:
            node,level = queue.popleft()
            if node:
                queue.append((node.left,level+1))
                queue.append((node.right,level+1))
                level_nodes[level].append(node.val)
        for i in range(level):
            ans.append(level_nodes[i])
        return ans
