# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode()
        curr = ret
        carry = 0

        while carry or l1 or l2:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next

            if s > 9:
                carry = s // 10
                s -= 10
            else: 
                carry = 0
            curr.val = s
            if carry > 0 or l1 or l2:
                curr.next = ListNode(s)
                curr = curr.next


        return ret




