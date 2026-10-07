# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ret = list()

        def helper(node, lvl):
            if not node:
                return

            if len(ret) <= lvl:
                ret.append([]) 
            ret[lvl].append(node.val)
            helper(node.left, lvl + 1)
            helper(node.right, lvl + 1)

        helper(root, 0)
        return ret




