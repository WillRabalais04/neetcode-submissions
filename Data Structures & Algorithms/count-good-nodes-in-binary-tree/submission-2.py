# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper(node, pm):
            if not node:
                return 0

            return (1 if node.val >= pm else 0) + helper(node.left, max(pm, node.val)) + helper(node.right, max(pm, node.val))

        
        return helper(root, root.val)

