class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ret = [0] * len(temperatures)

        stack = []
        for i,n in enumerate(temperatures):
            while stack and n > temperatures[stack[-1]]:
                prevIdx = stack.pop()
                ret[prevIdx] = max(0, i - prevIdx)
            stack.append(i)

        return ret
            