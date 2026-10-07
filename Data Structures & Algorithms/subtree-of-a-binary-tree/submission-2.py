# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def isIdenticalTree(r1, r2):
            if (not r1 and not r2):
                return True
            if (not r1 or not r2) or (r1.val != r2.val):
                return False

            return isIdenticalTree(r1.left, r2.left) and isIdenticalTree(r1.right, r2.right)

        def dfs(t, st):

            if not t or not st:
                return False

            if t.val == st.val:
                return isIdenticalTree(t,st) or dfs(t.left, st) or dfs(t.right, st)
            return dfs(t.left, st) or dfs(t.right, st)
            
        return dfs(root, subRoot)