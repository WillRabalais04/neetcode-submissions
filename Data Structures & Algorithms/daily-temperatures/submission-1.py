class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        results = len(temperatures) * [0]
        stack = []

        for idx, temp in enumerate(temperatures):
            a = str(stack[-1][1]) if stack else "n/a"
            print("temp: " + str(temp) + " | prevtemp: "  + a)
            while stack and temp > stack[-1][1]:
                prevIdx, prevTemp = stack.pop()
                results[prevIdx] += (idx - prevIdx)
            stack.append((idx, temp))

        return results



        