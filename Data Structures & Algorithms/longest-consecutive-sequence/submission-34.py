class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        nums = sorted(nums)

        # for i in range(len(nums) - 1, 0, -1):
        #     curr = nums[i]:
        #     while curr 
        # print(nums)
        ret = curr = 1
        prev = nums[0]
        
        # [2, 3, 4, 4, 5, 10, 20]
        # [2, 3, 4, 4, 5, 5, 10, 20]

        for i in range(1, len(nums)):
            if nums[i] == prev:
                continue

            if nums[i] > prev + 1:
                ret = max(curr, ret)
                curr = 0
            curr += 1

            prev = nums[i]
            # print(f"(i,n): ({i}, {nums[i]}) | curr: {curr}")
        
        ret = max(curr, ret)

        return ret
