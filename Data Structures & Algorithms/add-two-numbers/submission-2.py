# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = False
        ret = curr = ListNode(0)
        while l1 or l2:
            s = 0
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            s += (1 if carry else 0)
            carry = False
            if s >= 10:
                carry = True
                s -= 10
            curr.next = ListNode(s)
            curr = curr.next
        if carry:
            curr.next = ListNode(1)


        
        return ret.next
        
        