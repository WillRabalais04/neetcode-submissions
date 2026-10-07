class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # for each course: run dfs to validate prereq chains 
        # if valid course found return

        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[course].append(pre)
        print(adj)

        valid = []
        state = [0] * numCourses # 0=unvisited, 1=visiting, 2=visited

        def has_cycle(course):
            nonlocal valid
            if state[course] == 1: return True
            if state[course] == 2: return False
            
            state[course] = 1

            for prereq in adj[course]:
                if has_cycle(prereq):
                    return True
            
            state[course] = 2
            valid.append(course)
            
            return False

        for i in range(numCourses):
            if state[i] == 0 and has_cycle(i):
                return []

        return valid