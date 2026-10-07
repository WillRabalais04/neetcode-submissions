class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]

        def out_of_bounds(x,y) -> bool:
            return not ((0 <= x < m) and (0 <= y < n))
        def been_visited(x,y) -> bool:
            return visited[x][y] == 1

        def find_island_size(x,y) -> int:
            if out_of_bounds(x,y):
                return 0
            if grid[x][y] != 1 or been_visited(x,y):
                return 0
            visited[x][y] = 1
            left, right = find_island_size(x - 1,y), find_island_size(x + 1,y)
            up, down = find_island_size(x,y - 1), find_island_size(x,y + 1)
            return 1 + left + right + up + down
        
        island_size = max_island_size = 0
        for x in range(m):
            for y in range(n):
                if been_visited(x,y):
                    continue
                island_size = find_island_size(x,y)
                max_island_size = max(max_island_size, island_size)
                visited[x][y] = 1

        return max_island_size


        