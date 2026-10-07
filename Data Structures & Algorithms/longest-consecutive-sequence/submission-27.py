class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return len(nums)
        min_num = float('inf')
        max_num = float('-inf')
        for num in nums:
            min_num = min(min_num, num)
            max_num = max(max_num, num)

        contains = [0] * (max_num - min_num + 1)
        for i in range(len(nums)):
            idx = nums[i] - (min_num)
            contains[idx] = 1
        maxstreak = streak = 0
        print(contains)
        for i in range(len(contains)):
            print(i)
            streak = streak + 1 if contains[i] else 0
            maxstreak = max(maxstreak, streak)
        return maxstreak
        


        