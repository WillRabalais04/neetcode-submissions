class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) 

        for r in range(9):
            for c in range(9):
                t = board[r][c]
                if t == ".":
                    continue
                if (t in rows[r] or t in cols[c] or t in squares[(r // 3,c // 3)]) :
                    return False
                cols[c].add(t)
                rows[r].add(t)
                squares[(r // 3,c // 3)].add(t)

        return True