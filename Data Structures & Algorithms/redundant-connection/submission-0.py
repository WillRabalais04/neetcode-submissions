class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        cycle = set()
        cycleStart = -1
        ret = []

        def dfs(idx, pred):
            nonlocal cycleStart
            if idx in visited:
                # print(f"!! idx: {idx} | pred: {pred} | visited: {visited}")
                cycleStart = idx
                return True
            
            visited.add(idx) 

            for neighbor in adj[idx]:
                if neighbor == pred:
                    continue
                if dfs(neighbor, idx):
                    if cycleStart != -1:
                        cycle.add(idx)
                    if idx == cycleStart:
                        cycleStart = -1
                    return True
            return False

        dfs(1,-1)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
            
        return []