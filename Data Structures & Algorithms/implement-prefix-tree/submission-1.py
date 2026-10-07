class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.EOW = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            idx = ord(c) - 97
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.EOW = True
      
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            idx = ord(c) - 97
            if not node.children[idx]:
                return False
            node = node.children[idx]
        print(idx)
        return node.EOW

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            idx = ord(c) - 97
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True
        
        