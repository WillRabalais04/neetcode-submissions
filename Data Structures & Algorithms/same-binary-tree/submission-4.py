# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def DFS(n1,n2):
            if not n1 or not n2:
                return not n1 and not n2
            l = DFS(n1.left,n2.left)
            r = DFS(n1.right,n2.right) 
            return n1.val == n2.val and l and r
        return DFS(p,q)