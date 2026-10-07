class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        goalTotal = 0
        for i in range(len(nums)):
            total += nums[i] 
            goalTotal += (i + 1)


        return  goalTotal - total

        