# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast = slow = head

        if not head.next:
            return None

        while n > 0: # make fast n ahead of slow   
            fast = fast.next
            n -= 1

        if not fast: # n = length
            return head.next
        
        while fast: # get n to stop at 1 before 
            fast = fast.next
            if fast:
                slow = slow.next
        
        # if slow and slow.next: # skip 
        slow.next = slow.next.next

        return head