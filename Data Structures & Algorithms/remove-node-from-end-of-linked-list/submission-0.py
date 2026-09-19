# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        pre = dummy
        cur = head
        fast = head
        for _ in range(n):
            fast = fast.next
        while fast:
            pre = pre.next
            cur = cur.next
            fast = fast.next
        pre.next = cur.next
        return dummy.next