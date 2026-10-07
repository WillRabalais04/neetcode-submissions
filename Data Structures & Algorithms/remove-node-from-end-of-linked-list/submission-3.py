# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head.next: # empty list
            head = None
            return

        slow = head
        fast = head
        i = n
        while fast and i > 0: # fast is n nodes ahead of slow
            fast = fast.next
            i -= 1

        if not fast: # n = len
            head = head.next
        
        while fast: # stops when fast ends and skips a node, n nodes away from the end
            if not fast.next:
                slow.next = slow.next.next
                break
            slow = slow.next
            fast = fast.next

        return head
        

        
        