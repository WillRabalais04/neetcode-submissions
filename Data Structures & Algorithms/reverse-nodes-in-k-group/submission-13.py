# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)

        tail = dummy
        while True:
            kth = self.getKth(tail, k)
            if not kth:
                break
            
            nextGroup = kth.next
            prev, curr = kth.next, tail.next

            while curr != nextGroup:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = tail.next
            tail.next = kth
            tail = temp
            
        return dummy.next


    def getKth(self, node, k):
        cnt = k
        while cnt > 0 and node:
            node = node.next
            cnt -= 1
        return node