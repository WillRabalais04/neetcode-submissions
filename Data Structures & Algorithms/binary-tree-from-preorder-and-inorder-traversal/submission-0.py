# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build(po, io):
            if not po or not io:
                return None

            ridx = io.index(po[0])



            ioLeft = io[:ridx]
            ioRight = io[ridx + 1:]

            poLeft = po[1:1 + len(ioLeft)]
            poRight = po[1 + len(ioLeft):]

            print("val: " + str(po[0]) + "| poLeft: " + str(poLeft) + " | ioLeft: " + str(ioLeft) + " | poRight: " + str(poRight)+ " | ioRight: " + str(ioRight))

            return TreeNode(po[0], build(poLeft, ioLeft),build(poRight, ioRight))

        return build(preorder, inorder)

