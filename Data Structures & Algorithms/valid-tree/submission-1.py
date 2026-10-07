class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False

        state = [0] * n
        
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = {0}
        q = deque([0])

        while q:
            curr = q.popleft()
            for neighbor in adj[curr]:
                if not neighbor in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        
        return len(visited) == n

        #DFS
        # def has_cycles(idx):
        #     nonlocal q, state, adj
        #     if state[idx] == 1: return True
        #     if state[idx] == 2: return False
            
        #     q.append(idx)

        #     state[idx] = 1

        #     for neighbor in adj[idx]:
                

        #     while q:
        #         if has_cycles(q.pop()):
        #             return True

        #     state[idx] = 2

        #     return False

        # print(f"has_cycles(0): {has_cycles(0)} | state: {state} | sum(state) == 2 * n: {sum(state)}")
        # return not has_cycles(0) and sum(state) == 2 * n # might be redundant


        