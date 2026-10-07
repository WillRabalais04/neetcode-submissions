class PrefixTree:

    def __init__(self):
        self.tree = [None] * 26
        
    def insert(self, word: str) -> None:
        curr = self.tree
        for i, c in enumerate(word):
            idx = ord(c) - ord('a')
            if curr[idx] is None:
                curr[idx] = [PrefixTree(), False]
            if i == len(word) - 1:
                curr[idx][1] = True
            curr = curr[idx][0].tree

    def search(self, word: str) -> bool:
        curr = self.tree
        for i, c in enumerate(word):
            idx = ord(c) - ord('a')
            if curr[idx] is None:
                return False
            if i == len(word) - 1:
                return curr[idx][1]
            curr = curr[idx][0].tree

    def startsWith(self, prefix: str) -> bool:
        curr = self.tree
        for i, c in enumerate(prefix):
            idx = ord(c) - ord('a')
            if curr[idx] is None:
                return False
            curr = curr[idx][0].tree

        return True