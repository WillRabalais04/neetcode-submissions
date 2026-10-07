class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        col = set()
        pos_diag = set() # r + c
        neg_diag = set() # r - c
        
        ret = []
        board = [["."] * n for _ in range(n)]
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                ret.append(copy)
                return
            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                board[r][c] = "Q"
                backtrack(r + 1)

                col.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return ret
      
        '''
        one queen per row
        one queen per column
        one queen per diag
        '''




        '''
        n = 1:
        [["Q]]
        n = 2: DNE
        [[
            ..
            ..
        ]]
        n = 3: DNE
        [[
            ...
            ...
            ...
        ]]
        n = 4:
        [[
        ".Q..",
        "...Q",
        "Q...",
        "..Q."
        ],[
        "..Q.",
        "Q...",
        "...Q",
        ".Q.."
        ]]
        '''

