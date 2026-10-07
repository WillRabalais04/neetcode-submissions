# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        ret = []
        def dfs(node):
            nonlocal ret
            if not node:
                ret.append('-')
                return
            ret.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(ret)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = 0
        data = data.split(",")
        print(data)

        def dfs():
            nonlocal i
            if i >= len(data) or data[i] == '-':
                i += 1
                return None
            curr = data[i]
            print(curr)
            node = TreeNode(curr)
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()




