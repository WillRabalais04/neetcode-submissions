class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1] * len(nums)
        post = [1] * len(nums)
        ret = [1] * len(nums)

        for i in range(1, len(nums)):
            pre[i] *= nums[i-1] * pre[i -1]
        for i in range(len(nums) - 2, -1, -1):
            
            post[i] *= (nums[i+1] * post[i+1])
        for i in range(len(nums)):
            ret[i] = pre[i] * post[i]
        print(pre)
        print(post)

        return ret
        