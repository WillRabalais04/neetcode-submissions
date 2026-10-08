class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr in cols[c]:
                    print(f"curr: {curr} | cols[c]:{cols[c]}")
                    return False

                if curr in rows[r]:
                    print(f"curr: {curr} | rows[r]:{rows[r]}")
                    return False
                # sq_index instead of tuple becquse idk
                sq = ((r // 3) * 3) + (c // 3)
                if curr in squares[sq]:
                    print(f"curr: {curr} | cols[sq]:{squares[sq]}")
                    return False
                if curr != '.':
                    cols[c].add(curr)
                    rows[r].add(curr)
                    squares[sq].add(curr) 
        return True
                
  

        