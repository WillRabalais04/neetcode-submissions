class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        paths = []
        
        def dfs(idx, path):
            if idx in visited:
                return
            
            visited.add(idx)
            path.append(idx)

            for neighbor in adj[idx]:
                dfs(neighbor, path)

        count = 0

        for i in range(n):
            if i in visited:
                continue
            count += 1
            path = []
            dfs(i, path)
            paths.append(path)
            
        print(paths)

        return count
