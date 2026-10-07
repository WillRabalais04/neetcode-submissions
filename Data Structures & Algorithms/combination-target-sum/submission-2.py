class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        combinations = []
        subset = []
        def dfs(i):
            # print(sum(subset))
            if sum(subset) >= target:
                if sum(subset) == target and not subset in combinations:
                    combinations.append(subset.copy())
                return
            if i >= len(nums):
                return
            print(subset)
            subset.append(nums[i])
            dfs(i)
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        
        return combinations