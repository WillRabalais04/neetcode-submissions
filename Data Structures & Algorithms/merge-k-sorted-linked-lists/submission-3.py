# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists  = [l for l in lists if l]

        dummy = ListNode(0)
        curr = dummy

        while lists:
            minIndex = 0
            for i in range(1,len(lists)):
                if not lists[i]:
                    continue

                if lists[i].val < lists[minIndex].val:
                    minIndex = i
            
            curr.next = lists[minIndex]
            curr = curr.next

            lists[minIndex] = lists[minIndex].next

            if not lists[minIndex]:
                lists.pop(minIndex)

        return dummy.next