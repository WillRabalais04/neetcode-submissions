class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ret = [1] * len(nums)
        
        for idx in range (0, len(nums)):
            for idx2 in range (0, len(nums)):
                if(idx2 != idx):
                    ret[idx] *= nums[idx2]


        return ret
        