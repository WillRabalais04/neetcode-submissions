class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        
        # (pacific reachable, atlantic reachable)
        reachable = [[[False, False] for _ in range(cols)] for _ in range(rows)]

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(starts, ocean_index):
            q = deque(starts)
            while q:
                r,c = q.popleft()
                reachable[r][c][ocean_index] = True
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if reachable[nr][nc][ocean_index] or heights[nr][nc] < heights[r][c]:
                            continue
                        
                        reachable[nr][nc][ocean_index] = True
                        q.append((nr, nc))

        pacific_starts = []
        for r in range(rows): pacific_starts.append((r, 0))
        for c in range(cols): pacific_starts.append((0, c))
        bfs(pacific_starts, 0)

        atlantic_starts = []
        for r in range(rows): atlantic_starts.append((r, cols - 1))
        for c in range(cols): atlantic_starts.append((rows - 1, c))
        bfs(atlantic_starts, 1) 
        
        ret = []

        for r in range(rows):
            for c in range(cols):
                if reachable[r][c][0] and reachable[r][c][1]:
                    ret.append((r,c))

        return ret
