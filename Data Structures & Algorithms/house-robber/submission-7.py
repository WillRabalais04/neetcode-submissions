class Solution:
    def rob(self, nums: List[int]) -> int:
        
        scores = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if scores[i] != -1:
                return scores[i]
            scores[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return scores[i]
        return dfs(0)
#             [1,2,3,1]


#                   [3]  [3]  
# max()          [2]  [3]  [3]
#             [1]  [2]  [3]   [1]