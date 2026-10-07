# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ret = ""
        def dfs(node):
            nonlocal ret

            if not node:
                ret += "N,"
                return

            ret += str(node.val) + ","
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ret[:-1]
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # iterative recursion
        if len(data) < 1 or data[0] == "N":
            return
        
        data = data.split(",")
        print(data)

        idx = 0
        def dfs():
            nonlocal idx
            if idx >= len(data) or data[idx] == "N":
                return None
            node = TreeNode(data[idx])
            idx += 1
            node.left = dfs()
            idx += 1
            node.right = dfs()
            return node
        
        return dfs()



