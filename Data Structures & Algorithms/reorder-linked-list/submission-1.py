# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next # start of 2nd half of list
        prev = None
        slow.next = None

        while second: # reverse second
            temp = second.next 
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev
        while second: # merge lists
            t1 = first.next
            t2 = second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2