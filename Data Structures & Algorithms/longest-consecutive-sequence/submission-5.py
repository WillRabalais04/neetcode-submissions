class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        c = []
        for x in nums:
            if not (x in c):
                c.append(x)
        nums = sorted(c)

        maxendingati = [1] * len(nums)
        for i in range(1,len(nums)):
            if (nums[i] - nums[i-1] == 1):
                maxendingati[i] = maxendingati[i-1] + 1
        
        m = 0
        for x in maxendingati:
            if x > m:
                m = x

        return m


        