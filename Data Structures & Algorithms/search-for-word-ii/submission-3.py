class Trie:
    def __init__(self):
        self.tree = [None] * 26
        self.word =  None # used to mark EOW
    
    def insert(self, word):
        curr = self
        for c in word:
            idx = ord(c) - ord('a')
            if curr.tree[idx] is None:
                curr.tree[idx] = Trie()
            curr = curr.tree[idx]
        if word:
            curr.word = word
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        h, w = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)

        ret = list()
        
        def dfs(trie, pos, visited):
            nonlocal words
            c = board[pos[1]][pos[0]]
            idx = ord(c) - ord('a')
            if trie.tree[idx] is None:
                return
            trie = trie.tree[idx]
            if trie.word and trie.word not in ret:
                ret.append(trie.word)
                words.remove(trie.word)
            # print(f"x: {pos[0]} | y: {pos[1]} | c: { c} | tw: {trie.word} | ret: {ret} | visited: {visited}")
            up, down = (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)
            left, right = (pos[0] - 1, pos[1]), (pos[0] + 1, pos[1])
            
            # visited.add(pos)
            if up[1] >= 0 and up not in visited:
                dfs(trie, up,  visited | {pos})
            if down[1] < h and down not in visited:
                dfs(trie, down,  visited | {pos})
            if left[0] >= 0 and left not in visited:
                dfs(trie, left,   visited | {pos})
            if right[0] < w and right not in visited:
                dfs(trie, right,   visited | {pos})

        for y in range(h):
            for x in range(w):
                dfs(trie, (x,y), set())
            print(f"words: {words}\n")
            if len(words) == 0:
                return ret

        return ret

board=[
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]]



        