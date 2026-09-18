# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(next = head)
        slow = dummy
        fast = dummy
        while fast:
            if fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                break
        def reverse_nodes(head):
            if not head:
                return None
            if not head.next:
                return head
            pre = head
            cur = head.next
            pre.next = None
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre
        l2 = slow.next
        l2 = reverse_nodes(l2)
        l1 = head
        cur = dummy
        while l1 and l2:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
            cur.next.next = None
        return 