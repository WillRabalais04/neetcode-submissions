class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def mapIsland(x,y):
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or visited[y][x] or grid[y][x] == "0":
                return 0

            visited[y][x] = True
            mapIsland(x, y + 1) # up 
            mapIsland(x, y - 1) # down
            mapIsland(x - 1, y) # left
            mapIsland(x + 1, y) # right
            return 1

        islandCount = 0

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                islandCount += mapIsland(x,y)

        return islandCount

