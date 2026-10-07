class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        state = [0] * numCourses
        ret = []

        def has_cycle(idx):
            if state[idx] == 1: return True
            if state[idx] == 2: return False

            state[idx] = 1

            for prereq in adj_list[idx]:
                if has_cycle(prereq):
                    return True
            
            state[idx] = 2
            ret.append(idx)
            return False

        for i in range(numCourses):
            if state[i] == 0 and has_cycle(i):
                return []

        return ret