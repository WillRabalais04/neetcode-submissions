# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mp = float('-inf')
        def dfs(node):
            nonlocal mp
            if not node:
                return 0
            left, right = max(0, dfs(node.left)), max(0, dfs(node.right))
            curr = node.val + left + right
            mp = max(mp, curr)
            print(mp)
            return node.val + max(left, right)
        a = dfs(root)
        return mp


        