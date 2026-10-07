# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(PNode, QNode):
            if not PNode or not QNode:
                return not PNode and not QNode

            return PNode.val == QNode.val and dfs(PNode.left, QNode.left) and dfs(PNode.right, QNode.right)


        return dfs(p,q)
        