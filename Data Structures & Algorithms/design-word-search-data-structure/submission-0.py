class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.EOW = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.EOW = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if not node: 
                return False
            if idx == len(word):
                return node.EOW
            for i in range(idx, len(word)):
                if word[i] == '.':
                    for child in node.children:
                        if dfs(child, i + 1):
                            return True
                    return False
                else:
                    j = ord(word[i]) - ord('a')
                    if not node.children[j]:
                        return False
                    node = node.children[j]
            return node.EOW
                        
        return dfs(self.root, 0)
