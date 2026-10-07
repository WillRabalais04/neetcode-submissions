class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]

        def out_of_bounds(x,y) -> bool:
            return not ((0 <= x < m) and (0 <= y < n))
        def been_visited(x,y) -> bool:
            return visited[x][y] == 1

        def recurse_terrain(x,y, initial) -> int:
            if out_of_bounds(x,y) or been_visited(x,y) or grid[x][y] != initial:
                return 0
            visited[x][y] = 1
            left, right = recurse_terrain(x - 1,y, initial), recurse_terrain(x + 1,y, initial)
            up, down = recurse_terrain(x,y - 1, initial), recurse_terrain(x,y + 1, initial)
            return grid[x][y] + left + right + up + down
        
        island_size = max_island_size = 0
        for x in range(m):
            for y in range(n):
                if been_visited(x,y):
                    continue
                island_size = recurse_terrain(x,y, grid[x][y])
                max_island_size = max(max_island_size, island_size)

        return max_island_size


        