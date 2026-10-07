class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        permutation = []
        log = {k : False for k in nums}

        def dfs(i):
            if i >= len(nums):
                ret.append(permutation.copy())
                return
            for idx in range(len(nums)):
                if not permutation or not log[nums[idx]]:
                    permutation.append(nums[idx])
                    log[nums[idx]] = True
                    dfs(i + 1)
                    permutation.pop()
                    log[nums[idx]] = False

        dfs(0)

        return ret