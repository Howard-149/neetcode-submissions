"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        new_nodes = {}
        def dfs_build(root):
            if root not in new_nodes:
                new_node = Node(root.val)
                new_nodes[root] = new_node
                for node in root.neighbors:
                    dfs_build(node)
            return
        
        def dfs_clone(old_node):
            new_node = new_nodes[old_node]
            if not new_node.neighbors :
                for node in old_node.neighbors:
                    new_node.neighbors.append(new_nodes[node])
                    dfs_clone(node)
            return
        dfs_build(node)
        dfs_clone(node)
        return new_nodes[node]
