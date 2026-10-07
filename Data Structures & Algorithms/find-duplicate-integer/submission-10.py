class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # iterate thru nums, use indices as a frequency table
        for i in range(len(nums)):
            curr = abs(nums[i])
            if nums[curr - 1] > 0:
                nums[curr - 1] *= -1
            else:
                return curr
        return -1

