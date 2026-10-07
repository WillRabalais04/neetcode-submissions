# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxDiam = 0
        def DFS(node):
            nonlocal maxDiam
            if not node:
                return 0
            l,r = DFS(node.left), DFS(node.right)
            maxDiam = max(maxDiam, l + r)
            return 1 + max(l,r)

        DFS(root)
        return maxDiam

        