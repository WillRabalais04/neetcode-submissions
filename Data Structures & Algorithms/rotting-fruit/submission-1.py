class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        minutes = -1
        rows, cols = len(grid), len(grid[0])
        rotten = deque()
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        if fresh_count == 0:
            return 0
        neighbor_coords = [(-1,0),(1,0),(0,-1),(0,1)]
        while rotten:
            minutes += 1
            for _ in range(len(rotten)):
                r,c = rotten.popleft()
                print(f"minute: {minutes}")
                for row in grid:
                    print(row)
                for dr, dc in neighbor_coords:
                    nr,nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        fresh_count -= 1
                        grid[nr][nc] = 2
                        rotten.append((nr,nc))

        if fresh_count:
            return -1

        return minutes

        



