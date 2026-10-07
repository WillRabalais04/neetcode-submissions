class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ret = []

        def dfs(s, idx):
            if idx >= len(nums):
                ret.append(s)
                return
            dfs(s + [nums[idx]], idx + 1)
            dfs(s, idx + 1)

        dfs([], 0)
        return ret