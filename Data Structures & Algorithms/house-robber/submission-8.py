class Solution:
    def rob(self, nums: List[int]) -> int:
        
        scores = [-1] * len(nums) # holds max total score if i is considered in the heist (max propagates backwards)

        def dfs(i):
            if i >= len(nums):
                return 0
            if scores[i] != -1:
                return scores[i]
            scores[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            print(scores)
            return scores[i]
        return dfs(0)