class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        ret = []

        def dfs(idx, cs, arr):
            if cs == target:
                ret.append(arr[:])
                return
            for i in range(idx, len(nums)):
                if cs + nums[i] > target:
                    break
                arr.append(nums[i])
                dfs(i, cs + nums[i], arr)
                arr.pop()

        dfs(0, 0, [])
        return ret
        