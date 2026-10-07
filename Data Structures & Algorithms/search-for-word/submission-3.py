class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h,w = len(board), len(board[0])
        visited = set()
        
        def search():
            for y in range(h):
                for x in range(w):
                    if backtrack(0, (x,y)):
                        return True
            return False

        def backtrack(i, coords):
            if coords in visited:
                return False
            x,y = coords[0], coords[1]
            if word[i] != board[y][x]:
                return False
            if i == (len(word) - 1):
                return True

            visited.add((x,y))
            if (y-1) >= 0 and backtrack(i + 1, (x, y-1)): # up
                return True
            if (y+1) < h and backtrack(i + 1, (x, y+1)): # down
                return True
            if (x-1) >= 0 and backtrack(i + 1, (x-1, y)): # left 
                return True
            if (x+1) < w and backtrack(i + 1, (x+1, y)): # right
                return True
            visited.remove((x,y))
            return False  

        return search()
        