class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ret = []

        def dfs(idx, arr):
            if idx == len(nums):
                ret.append(arr[:])
                return
            arr.append(nums[idx])
            dfs(idx + 1, arr)
            arr.pop()
            dfs(idx + 1, arr)

        dfs(0,[])
        return ret