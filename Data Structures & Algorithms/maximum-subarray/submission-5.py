class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        r = 1
        ret = curr = nums[0]

        while r < len(nums):
            print(f"cs:{curr} | r: {r}")
            if curr < 0:
                curr = 0
            curr += nums[r]
            r += 1
            ret = max(ret, curr)

        return ret
        
        