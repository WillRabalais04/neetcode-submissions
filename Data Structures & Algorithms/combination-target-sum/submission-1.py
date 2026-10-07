class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        comb = []
        nums.sort()

        def dfs(i, t):
            if t == target:
                ret.append(comb.copy())
                return

            for j in range(i, len(nums)):
                if t + nums[i] > target:
                    return
                comb.append(nums[j])
                dfs(j, t + nums[j])
                comb.pop()
        
        dfs(0,0)
        return ret