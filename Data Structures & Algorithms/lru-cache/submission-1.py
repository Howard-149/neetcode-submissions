class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.node_map = {}
        self.capacity = capacity
        self.dummy = Node()
        self.right = self.dummy
        self.cur_len = 0

    def get(self, key: int) -> int:
        if key in self.node_map:
            node = self.node_map[key]
            if node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.prev = self.right
                node.next = None
                self.right.next = node
                self.right = node 
        return self.cache.get(key,-1)

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            node = self.node_map[key]
            if node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.prev = self.right
                node.next = None
                self.right.next = node
                self.right = node
        else:
            node = Node(key,next = None, prev = self.right)
            self.node_map[key] = node
            self.right.next = node
            self.right = node
            self.cur_len+=1
            if self.cur_len > self.capacity:
                del_key = self.dummy.next.val
                self.node_map.pop(del_key)
                self.cache.pop(del_key)
                self.dummy.next = self.dummy.next.next
                self.dummy.next.prev = self.dummy   
        self.cache[key] = value
