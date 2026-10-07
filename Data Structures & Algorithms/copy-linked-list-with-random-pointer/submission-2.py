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
        
        cache = dict()
        def copyRandomListHelper(h):
            if not h:
                return None
            if h in cache:
                return cache[h]
            
            new_node =  Node(h.val) 
            cache[h] = new_node
            new_node.next = copyRandomListHelper(h.next)
            new_node.random = copyRandomListHelper(h.random)

            return new_node

        return copyRandomListHelper(head)



        