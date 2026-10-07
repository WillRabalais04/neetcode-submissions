class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ret = []
        c = []
        nums.sort()

        def dfs(i, s):
            if s == target:
                ret.append(c.copy())
                return
 
            for j in range(i, len(nums)):
                if s + nums[j] > target:
                    return
                c.append(nums[j])
                dfs(j, s + nums[j])
                c.pop()
        dfs(0,0)

        return ret