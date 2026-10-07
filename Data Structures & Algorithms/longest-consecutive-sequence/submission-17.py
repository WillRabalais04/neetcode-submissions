class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0
        min_n = min(nums) #O(n)
        if min_n < 0:
            for i in range(len(nums)):
                nums[i] += abs(min_n)
        print(nums)

        max_n = max(nums) 
        freq = [0] * (max_n + 1)
        count = ret = 0
        for num in nums: 
            freq[num] = 1
        for n in freq:
            if n == 0:
                count = 0
            else:
                count += 1
            ret = max(ret, count)
        print(nums)
        print(freq)
        return ret