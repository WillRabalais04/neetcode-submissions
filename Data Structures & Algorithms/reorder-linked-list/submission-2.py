# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast = mid = head

        while fast and fast.next: # find middle index
            mid = mid.next
            fast = fast.next.next

        prev = None
        curr = mid.next
        mid.next = None
        while curr: # reverse 2nd half
            temp = prev
            prev = curr
            curr = curr.next
            prev.next = temp

        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2


        


        