class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        arr = []
        visited = [False] * len(nums)

        def dfs(idx):
            if idx >= len(nums):
                ret.append(arr[:])
                return
            for i in range(len(nums)):
                if not visited[i]:
                    arr.append(nums[i])
                    visited[i] = True
                    dfs(idx + 1)
                    arr.pop()
                    visited[i] = False
            
        dfs(0)
        return ret