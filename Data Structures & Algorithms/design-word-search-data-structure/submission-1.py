class WordDictionary:

    def __init__(self):
        self.tree = [None] * 26
        self.EOW = False

    def addWord(self, word: str) -> None:
        curr = self.tree
        for i,c in enumerate(word):
            idx = ord(c) - ord('a')
            if curr[idx] is None:
                curr[idx] = WordDictionary()
            if i == len(word) - 1:
                curr[idx].EOW = True
            curr = curr[idx].tree

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word): 
                return node.EOW
            if word[i] == ".":
                for child in node.tree:
                    if child and dfs(child, i + 1):
                        return True
                return False
            else:
                idx = ord(word[i]) - ord('a')
                if node.tree[idx] is None:
                    return False
                return dfs(node.tree[idx], i + 1)
                
        return dfs(self, 0)