class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = 0

        for i in range(len(nums)):
            a ^= (i+1) ^ nums[i]

        return a

        