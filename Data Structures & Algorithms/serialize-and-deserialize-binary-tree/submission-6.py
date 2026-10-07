# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def helper(node):
            if not node:
                return ""
            return str(node.val) + helper(node.left) + helper(node.right)
        
        return helper(root)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        # stack = []
        # while stack or data:
        #     node = TreeNode()
        #     while stack:
        #         node.left = stack.pop()






        return root
