# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = l1
        b = l2
        c = 0
        dummy = ListNode(0)
        cur = dummy
        while a or b or c:
            if a:
                A = a.val
            else:
                A = 0
            if b:
                B = b.val
            else:
                B = 0
            val = (A+B+c)%10
            c = (A+B+c)//10
            cur.next = ListNode(val)
            if a:
                a = a.next
            if b:
                b = b.next
            cur = cur.next
        return dummy.next