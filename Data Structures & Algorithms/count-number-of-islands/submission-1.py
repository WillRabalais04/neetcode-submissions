class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if len(grid) == 0:
            return 0

        w,h = len(grid[0]), len(grid)

        visited = [[False] * w for _ in range(h)]
        
        def find_island(x,y):
            if (not (0 <= x < w)) or (not (0 <= y < h)) or visited[y][x] or grid[y][x] == "0":
                return 0
            
            visited[y][x] = True
            find_island(x, y-1) # up
            find_island(x, y+1) # down
            find_island(x-1, y) # left
            find_island(x+1, y) # right
            return 1
        
        count = 0
        for y in range(h):
            for x in range(w):
                count += find_island(x,y)
        
        return count



            