# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # if lists == []:
        #     return []
        # if len(lists) == 1:
        #     return lists[0]

        ret = ListNode(0)
        curr = ret

        while True:
            minIdx = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minIdx == -1 or lists[i].val < lists[minIdx].val:
                    minIdx = i
            if minIdx == -1:
                break
            
            curr.next = lists[minIdx]
            lists[minIdx] = lists[minIdx].next
            curr = curr.next

        return ret.next
        