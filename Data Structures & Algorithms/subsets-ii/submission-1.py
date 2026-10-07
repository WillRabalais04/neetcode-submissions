class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ret = []
        nums.sort()
        def dfs(path, idx):
            print(path)
            ret.append(path[:])  
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    print(i)
                    continue
                dfs(path + [nums[i]], i + 1)

        dfs([],0)
        return ret
        