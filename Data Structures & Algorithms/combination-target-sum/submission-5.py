class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ret = []
        def dfs(s, idx, arr):
            if s > target or idx >= len(nums): 
                return
            if s == target:
                ret.append(arr)
                return
            
            dfs(s, idx + 1, arr)
            dfs(s + nums[idx], idx, arr + [nums[idx]])

            #         this, next
            #      add c     c
            # dont add il    c

        dfs(0,0,[])
        return ret
        