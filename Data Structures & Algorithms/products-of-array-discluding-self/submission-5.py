class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ret = [1] * len(nums)
        pre = post = 1

        for i in range(len(nums)):
            ret[i] *= pre
            pre *= nums[i]
        for i in range(len(nums) -1, -1, -1):
            ret[i] *= post
            post *= nums[i]
        return ret