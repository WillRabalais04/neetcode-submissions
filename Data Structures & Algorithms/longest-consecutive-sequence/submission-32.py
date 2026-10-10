class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        nums = sorted(nums)
        print(nums)
        prev = nums[0]
        ret = 0

        for i in range(1, len(nums)):
            if nums[i] > prev + 1:
                print(f"nums[i]: {nums[i]}")
                break
            prev = nums[i]
            ret += 1

        return ret