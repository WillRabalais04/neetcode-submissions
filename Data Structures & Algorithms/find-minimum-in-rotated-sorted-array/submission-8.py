class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        m = 1000

        while l <= r:
            k = (l + r) // 2
            m = min(nums[k], m)

            if (k < len(nums) - 1) and nums[k] > nums[k + 1]:
                return nums[k + 1]

            if nums[k] > nums[r]:
                l = k + 1
            else:
                r = k - 1

        return m