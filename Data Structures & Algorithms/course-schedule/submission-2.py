class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[course].append(pre)
        
        state = [0] * numCourses

        def has_cycle(u):
            if state[u] == 1: return True
            if state[u] == 2: return False
            
            state[u] = 1
            for v in adj[u]:
                if has_cycle(v):
                    return True
            
            state[u] = 2
            return False

        for i in range(numCourses):
            if state[i] == 0:
                if has_cycle(i):
                    return False
        
        return True