class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h,w = len(board), len(board[0])
        visited = set()
        
        def search():
            for y in range(h):
                for x in range(w):
                    print(f"x,y = {x},{y} | {board[y][x]}")
                    if backtrack(0, (x,y)):
                        print("!!!!!!!")
                        return True
                    print()
            return False

        def backtrack(i, coords):
            if coords in visited:
                return False
            x,y = coords[0], coords[1]
            print(f"bb x,y = {x},{y} | {board[y][x]} |  word[i] {word[i]}")
            if word[i] != board[y][x]:
                return
            if i == (len(word) - 1):
                return True
            # print(word[i])

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

["A","B","C","E"],
["S","F","C","S"],
["A","D","E","E"]
            
        