# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        head = curr = ListNode()
        if len(lists) == 0:
            return ListNode().next
        elif len(lists) == 1:
            return lists[1]

        while len(lists) > 1:
            idx = 0
            for i in range(1,len(lists)):
                if lists[i].val < lists[idx].val:
                    idx = i

            temp = lists[idx].next
            lists[idx].next = None
            curr.next = lists[idx]
            if temp is None:
                lists.pop(idx)
            else:
                lists[idx] = temp
            curr = curr.next
        
        if lists[0] is None:
            lists.pop(0)
        else:
            curr.next = lists[0]

        return head.next
