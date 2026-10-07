# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def handleCarry(s,c):
            res = 0
            if s + c >= 10:
                return (s + c) % 10, (s + c) // 10
            else:
                return s + c, 0
            
        s = ListNode()
        h = s
        carry = 0

        while l1 and l2:     
            s.val, carry = handleCarry(l1.val + l2.val, carry)
            l1 = l1.next
            l2 = l2.next
            s.next = ListNode()
            if l1 and l2:
                s = s.next
        s.next = l1 or l2

        while carry > 0:
            res = 0
            if l1:
                res += l1.val
                l1 = l1.next
            elif l2:
                res += l2.val
                l2 = l2.next
            res,carry = handleCarry(res,carry)
            s.next = ListNode(res)
            s = s.next
        
        return h