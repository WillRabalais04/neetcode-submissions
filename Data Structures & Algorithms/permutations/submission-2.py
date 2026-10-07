class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        permutation = []
        log = [False] * len(nums)

        def dfs(i):
            if i >= len(nums):
                ret.append(permutation.copy())
                return
            for idx in range(len(nums)):
                if not log[idx]:
                    permutation.append(nums[idx])
                    log[idx] = True
                    dfs(i + 1)
                    permutation.pop()
                    log[idx] = False
        dfs(0)

        return ret