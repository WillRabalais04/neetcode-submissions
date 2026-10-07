class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in range(len(nums)):
            a ^= (i+1)
            b ^= nums[i]
        print(a)
        print(b)
        return a ^ b

        