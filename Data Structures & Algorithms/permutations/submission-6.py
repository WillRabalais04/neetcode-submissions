class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        visited = set()
        path = []
        ret = []

        def dfs(idx):
            if idx >= len(nums):
                ret.append(path[:])
                return
            for i in range(len(nums)):
                print(f"visited: {visited} | idx: {idx} | i: {i} | path: {path}")
                if i not in visited:
                    visited.add(i)
                    path.append(nums[i])
                    dfs(idx + 1)
                    path.pop()
                    visited.remove(i)

        dfs(0)
        return ret
        