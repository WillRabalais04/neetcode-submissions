# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ml = []
        def maxDepthHelper(x, length):
            if not x:
                ml.append(length)
                return
            maxDepthHelper(x.left, length + 1)
            maxDepthHelper(x.right, length + 1)
        
        maxDepthHelper(root, 0)
        return max(ml)   