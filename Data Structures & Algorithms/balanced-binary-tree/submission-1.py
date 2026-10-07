# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def DFS(node):

            if not node:
                return 0, True

            l,r = DFS(node.left) , DFS(node.right)

            return max(l[0],r[0]) + 1, l[1] and r[1] and abs(r[0] - l[0]) < 2
        
        

        return DFS(root)[1]