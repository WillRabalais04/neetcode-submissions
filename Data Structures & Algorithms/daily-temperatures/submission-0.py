class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ret = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                index,temp = stack.pop()
                ret[index] = i - index
            stack.append((i,t))
        
        return ret


        

        