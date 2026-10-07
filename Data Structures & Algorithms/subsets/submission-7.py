class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ret = []
        def dfs(arr, idx):
            if idx == len(nums):
                ret.append(arr)
                return
            dfs(arr, idx + 1)
            dfs(arr + [nums[idx]], idx + 1)

        dfs([], 0)
        return ret
        