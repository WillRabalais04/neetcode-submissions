class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ret = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  
                continue
            target = -nums[i]
            # arr = nums[:i] + nums[i + 1:]
            l,r = i + 1, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                   l += 1
                elif s > target:
                    r -= 1
                else:
                    ret.append([-target, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l+=1
                    r-=1
        return ret
        