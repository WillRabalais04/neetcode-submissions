# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        
        head = curr = ListNode()

        while len(lists) > 1:
            midx = 0
            for i in range(1,len(lists)):
                if lists[i].val < lists[midx].val:
                    midx = i

            temp = lists[midx].next
            lists[midx].next = None
            curr.next = lists[midx]
            if temp is None:
                lists.pop(midx)
            else:
                lists[midx] = temp
            curr = curr.next

        curr.next = lists[0]

        return head.next
