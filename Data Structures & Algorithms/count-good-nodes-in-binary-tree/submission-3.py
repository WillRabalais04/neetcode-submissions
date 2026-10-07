# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, prevMax):
            if not node:
                return 0
            greater = 0
            if node.val >= prevMax:
                prevMax = node.val
                greater = 1
            l,r = dfs(node.left, prevMax), dfs(node.right, prevMax)

            return l + r + greater
        

        return dfs(root, -101)

