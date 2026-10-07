# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        curr = head

        while list1 or list2:
            m = float('inf')
            if list1 and list2:
                if list1.val < list2.val:
                    m = ListNode(list1.val)
                    list1 = list1.next
                else:
                    m = ListNode(list2.val)
                    list2 = list2.next
            elif list1:
                m = ListNode(list1.val)
                list1 = list1.next
            elif list2:
                m = ListNode(list2.val)
                list2 = list2.next

            curr.next = m
            curr = curr.next
        
        return head.next