class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        al = [[] for _ in range(numCourses)]

        for i in range(len(prerequisites)):
            a,b = prerequisites[i][0], prerequisites[i][1]
            al[a].append(b)
        
        for row in al:
            print(row)
        
        state = [0] * numCourses
        '''
        0 : unvisited
        1 : visiting
        2 : visited
        '''

        course_count = 0

        def dfs(course):
            nonlocal course_count
            if state[course] == 2:
                return True
            course_count += 1
            if state[course] == 1:
                # cycle detected
                return False
            state[course] = 1

            valid_prereq_chain = True
            for prereq in al[course]:
                valid_prereq_chain = valid_prereq_chain and dfs(prereq)
            state[course] = 2
            return valid_prereq_chain


        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return False

        return course_count >= numCourses