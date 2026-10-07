class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if len(nums) < 2:
            return [0]
        
        l = r = 1
        ret = [1] * len(nums)
        
        for i in range(len(nums)):

            lidx = i - 1
            ridx = len(nums) - i

            if lidx > -1:
                l *= nums[lidx]
                ret[i] *= l

            if ridx < len(nums):
                r *= nums[ridx]
                ret[len(nums) - i - 1] *= r

        return ret