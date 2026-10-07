class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[course].append(pre)

        '''
        state tracking: 
        - 0: not visited
        - 1: visiting
        - 2: visited 
        '''

        state = [0] * numCourses

        def detect_cycle(course):
            if state[course] == 1: return True
            if state[course] == 2: return False

            state[course] = 1

            for prereq in adj[course]:
                if detect_cycle(prereq):
                    return True

            state[course] = 2
            return False

        for i in range(numCourses):
            if state[i] == 0:
                if detect_cycle(i):
                    return False
        return True


        