# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def IsSameTree(p,q):
            if not p or not q:
                return not p and not q
            if p.val != q.val:
                return False
            l,r = IsSameTree(p.left, q.left), IsSameTree(p.right, q.right)

            return l and r

        def DFS(node):
            if not node:
                return False

            return IsSameTree(node,subRoot) or DFS(node.left) or DFS(node.right)


        return DFS(root)




