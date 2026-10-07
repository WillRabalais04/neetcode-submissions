class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if len(nums) < 2:
            return 0

        out = [1] * len(nums)

        l = r = 1

        # for i in range(1, len(nums)):
        #     l *= nums[i - 1]
        #     out[i] *= l
        # for i in range(len(nums) -2, -1, -1):
        #     r *= nums[i + 1]
        #     out[i] *= r

        # out[0] *= nums[-1]
        # out[-1] *= nums[0]
        
        for i in range(len(nums)):
            lidx = i - 1
            ridx = len(nums) - i
            if lidx > -1:
                l *= nums[lidx]
                out[i] *= l
            if ridx < len(nums):
                r *= nums[ridx]
                out[len(nums) - i - 1] *= r


        return out