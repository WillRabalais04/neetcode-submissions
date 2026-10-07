# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        ll = []
        def helper(node, lvl):
            if not node:
                return
            print("v: " + str(node.val) + " | ll: " + str(ll))
            if lvl not in ll:
                ll.append(lvl)
                ret.append(node.val)

            helper(node.right, lvl + 1)
            helper(node.left, lvl + 1)

        helper(root, 0)
        return ret