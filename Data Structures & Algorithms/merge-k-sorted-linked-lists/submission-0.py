# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def printLL(ll):
            s = ""
            curr = ll
            while curr:
                s += str(curr.val) 
                curr = curr.next
            print(s)

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        ret = ListNode(0)
        curr = ret

        while True: #O(n)
            minIndex = -1
            for i in range(len(lists)): # O(k)
                if not lists[i]:
                    continue
                if minIndex == -1 or lists[i].val < lists[minIndex].val:
                    minIndex = i

            if minIndex == -1:
                break
            curr.next = lists[minIndex]
            lists[minIndex] = lists[minIndex].next
            curr = curr.next

        return ret.next

        '''
        [[1,2,4],[1,3,5],[3,6]]
          _
        [[1,2,4],[1,3,5],[3,6]]
            _   
        [[1,1,2,4],[3,5],[3,6]]
              _   
        [[1,1,2,4],[3,5],[3,6]]
                _  
        [[1,1,2,3,4],[5],[3,6]]
                  _  
        [[1,1,2,3,3,4],[5],[6]]
                    _  
        [[1,1,2,3,3,4,5],None,[6]]
                      _  
        [[1,1,2,3,3,4,5,6],None,None]
                      _  

                 # O(1) space means reuse given array
        # findNextPlace
        
        # [[3,6],[1,2,4],[1,3,5]]
        #   _
        # [[1,3,6],[1,2,4],[3,5]]
        #   _
        # [[1,1,3,6],[2,4],[3,5]]
        #     _
        # [[1,1,2,3,6],[4],[3,5]]
        #       _
        # [[1,1,2,3,3,6],[4],[5]]
        #           _
        # [[1,1,2,3,3,3,4,6],[],[5]]
        #             _
        # [[1,1,2,3,3,3,4,5,6],[]]
        #               _
        # [[1,1,2,3,3,3,4,5,6]]
        #                 _                   
        '''

    