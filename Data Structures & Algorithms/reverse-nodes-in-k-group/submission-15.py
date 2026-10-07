# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def printLL(h):
            while h:
                print(h.val)
                h = h.next
            print("\n")

        def reversedListTail(h):
            curr = h
            prev = None
            while curr:
                temp = prev
                prev = curr
                curr = curr.next
                prev.next = temp
            return prev, h 
        
        def jumpAheadByK(h, c):
            a = h
            while c > 1:
                if not a:
                    return None
                a = a.next
                c -= 1
            return a

        slow = head
        fast = jumpAheadByK(slow, k)
        newHead = None 
        prevTail = None

        while slow and fast:
            temp = fast.next # separate new list
            fast.next = None 
            
            revHead, revTail = reversedListTail(slow)
            
            if not newHead:
                newHead = revHead
           
            if prevTail:
                prevTail.next = revHead
            
            revTail.next = temp 
            prevTail = revTail  

            slow = temp
            fast = jumpAheadByK(slow, k)

        return newHead if newHead else head