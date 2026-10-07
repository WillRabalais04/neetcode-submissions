# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # curr: 0->1->2->3
        # prev: None

        # curr: 1->2->3
        # prev: 0

        # curr: 2->3
        # prev: 1->0

        # curr: 3
        # prev: 2->1->0

        # curr: None
        # prev: 3->2->1->0
     
        # 0
        # 1->0
        # 2->1->0
        # 3->2->1->0


        prev = None
        curr = head
        
        while curr:
            temp = prev
            prev = curr
            curr = curr.next
            prev.next = temp


        return prev


        