class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        combinations = []
        subset = []
        def dfs(i, cs):
            print(subset)
            if cs == target:
                combinations.append(subset.copy())
                return
            if i >= len(nums) or cs > target:
                return

            subset.append(nums[i])
            dfs(i, cs + nums[i])
            subset.pop()
            dfs(i + 1, cs)

        dfs(0, 0)
        
        return combinations