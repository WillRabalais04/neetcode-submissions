class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False
        
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # BFS
        # visited = {0}
        # q = deque([0])

        # while q:
        #     curr = q.popleft()
        #     for neighbor in adj[curr]:
        #         if not neighbor in visited:
        #             visited.add(neighbor)
        #             q.append(neighbor)
        
        # return len(visited) == n

        # DFS
        state = [0] * n
        def has_cycle(idx, parent):
            state[idx] = 1
            for neighbor in adj[idx]:
                if parent is not None and neighbor == parent:
                    continue
                
                if state[neighbor] == 1: 
                    return True
                
                if state[neighbor] == 0:
                    if has_cycle(neighbor, idx):
                        return True
                    
            state[idx] = 2
            return False
        
        for i in range(n):
            if has_cycle(i, None):
                print(f"dinding: {i}")
                return False
        
        print(f"state: {state}")

        return sum(state) == 2 * n