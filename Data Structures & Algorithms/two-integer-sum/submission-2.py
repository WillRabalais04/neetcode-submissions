class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complement = dict()

        for i in range(0,len(nums)):
            c = target - nums[i]
            if nums[i] in complement:
                return [complement[nums[i]], i]
            complement[c] = i
        
        return [0,0]


        