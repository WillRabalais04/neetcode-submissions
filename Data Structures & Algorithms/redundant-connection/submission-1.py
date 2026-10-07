class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        cycle = set()
        cycle_start = -1
        ret = []

        def dfs(node, pred):
            nonlocal cycle_start

            if node in visited:
                cycle_start = node
                return True
            
            visited.add(node)

            for n in adj[node]:
                if n == pred:
                    continue

                if dfs(n, node):
                    if cycle_start != -1:
                        cycle.add(node)
                    if node == cycle_start:
                        cycle_start = -1
                    return True
            return False


        dfs(1,-1)

        for a,b in reversed(edges):
            if a in cycle and b in cycle:
                return [a,b]

        return []
        