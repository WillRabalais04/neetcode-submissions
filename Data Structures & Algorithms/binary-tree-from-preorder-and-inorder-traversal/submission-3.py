# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        pidx = iidx = 0

        def dfs(lim):
            nonlocal pidx, iidx
            if pidx >= len(preorder) or inorder[iidx] == lim:
                return None
            root_val = preorder[pidx]
            pidx += 1
            
            node = TreeNode(root_val)
            node.left = dfs(root_val)

            iidx += 1
            node.right = dfs(lim)
            return node
            
        return dfs(float('inf'))