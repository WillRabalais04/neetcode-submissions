"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # fancy interleaving version
        if not head:
            return None
        curr = head
        while curr: # go from A->B->C to A'->B'->C'
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        curr = head
        while curr: # adding random pointers
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # separating copy list

        curr = head
        copy_head = head.next
        copy_curr = copy_head

        while curr:
            curr.next = curr.next.next
            if copy_curr.next:
                copy_curr.next = copy_curr.next.next
            copy_curr = copy_curr.next
            curr = curr.next

        return copy_head


        