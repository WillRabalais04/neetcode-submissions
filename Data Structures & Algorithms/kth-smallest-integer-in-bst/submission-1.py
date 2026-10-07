# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ret = []
        count = k
        el = -1
        def DFS(node):
            nonlocal count, el
            if not node:
                return
            DFS(node.left)
            count -= 1
            if count == 0:
                el = node.val
                return
            DFS(node.right)
        
        DFS(root)
        return el


        