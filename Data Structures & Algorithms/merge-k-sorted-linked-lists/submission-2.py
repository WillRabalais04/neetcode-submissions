class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Remove empty lists
        lists = [l for l in lists if l]
        
        if not lists:
            return None
        
        # Initialize a dummy head to simplify merging
        dummy = ListNode(0)
        tail = dummy
        
        # Continue until all lists are exhausted
        while lists:
            # Find minimum head
            min_index = 0
            for i in range(1, len(lists)):
                if lists[i].val < lists[min_index].val:
                    min_index = i
            
            # Attach minimum node to result
            tail.next = lists[min_index]
            tail = tail.next
            
            # Move the list forward
            lists[min_index] = lists[min_index].next
            
            # Remove list if exhausted
            if not lists[min_index]:
                lists.pop(min_index)
        
        return dummy.next