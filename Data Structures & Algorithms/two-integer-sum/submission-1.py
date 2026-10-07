class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        i = -1
        for x in range(len(nums)):
            if nums[x] < target:
                i = nums[x]
            for y in range(x + 1,len(nums)):
                if nums[x] + nums[y] == target:
                    ret.append(x)
                    ret.append(y)
                    return ret

        