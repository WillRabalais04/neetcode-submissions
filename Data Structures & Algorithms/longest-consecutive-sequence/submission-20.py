class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
      
        nums.sort()

        streak = maxstreak = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            streak = streak + 1 if nums[i] == nums[i-1] + 1 else 1
            maxstreak = max(maxstreak, streak)
        return maxstreak