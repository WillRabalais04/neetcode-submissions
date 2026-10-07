class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ret = []
        visited = [False] * len(nums)
        path = []
        
        def dfs(idx):
            if idx >= len(nums):
                ret.append(path[:])
                return
            for i in range(len(nums)):
                if not visited[i]:
                    path.append(nums[i])
                    visited[i] = True
                    dfs(idx + 1)
                    path.pop()
                    visited[i] = False

        dfs(0)
        return ret
        