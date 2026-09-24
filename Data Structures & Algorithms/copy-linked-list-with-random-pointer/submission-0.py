"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        Node_Hash = {}
        dummy = Node(0)
        new = dummy
        cur = head
        while cur:
            new_node = Node(cur.val,cur.next)
            new.next = new_node
            Node_Hash[cur] = new_node
            new = new.next
            cur = cur.next
        cur = head
        new = dummy.next
        while cur:
            if cur.random:
                new_random = Node_Hash[cur.random]
                new.random = new_random
            new = new.next
            cur = cur.next
        return dummy.next
            
        