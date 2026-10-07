class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l <= r:
            mp = (l + r) // 2
            if nums[mp] == target:
                return mp
            if nums[l] <= nums[mp]:
                if target > nums[mp] or target < nums[l]:
                    l = mp + 1
                else:
                    r = mp - 1
            else:
                if target < nums[mp] or target > nums[r]:
                    r = mp - 1
                else:
                    l = mp + 1

        return -1


        
        

        