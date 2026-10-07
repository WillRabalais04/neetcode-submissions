class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ret = [1] * len(nums)
        prefix = 1
        for idx in range(0, len(nums)):
            ret[idx] *= prefix
            prefix *= nums[idx]
        postfix = 1
        for idx in range(len(nums) - 1, -1, -1):
            ret[idx] *= postfix
            postfix *= nums[idx]

        return ret