class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for row in board:
            print(row)
        print("")
        
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        surrounded = []

        def is_an_edge(r,c):
            return r == 0 or r == rows - 1 or c == 0 or c == cols -1

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def is_surrounded(r,c):
            visited[r][c] = True
            ret = ret = not is_an_edge(r, c)

            for dr, dc in directions:
                nr,nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and board[nr][nc] == 'O':
                    iss = is_surrounded(nr,nc)
                    ret = ret and iss
            return ret

        def fill(r,c):
            board[r][c] = "X"
            for dr, dc in directions:
                nr,nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    fill(nr,nc)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and not visited[r][c]:
                    if is_surrounded(r, c):
                        fill(r, c)

        for row in board:
            print(row)