class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        minutes = -1
        rotten = deque()
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        
        # find rotten
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rotten.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while rotten:
            minutes += 1
            for _ in range(len(rotten)):
                r,c = rotten.popleft()
                for dr,dc in directions:
                    nr,nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            fresh_count -= 1
                            grid[nr][nc] = 2
                            rotten.append((nr,nc))

        if fresh_count:
            return -1

        return minutes

        