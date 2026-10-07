class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l <= r:
            mp = (l + r) // 2
            if nums[mp] == target:
                return mp
            if nums[l] <= nums[mp]: # pivot is to the right
                if target > nums[mp] or target < nums[l]: # target to right of mp
                    l = mp + 1
                else:  
                    r = mp - 1
            else: # pivot is to the left
                if target < nums[mp] or target > nums[r]: # target to left of mp
                    r = mp - 1
                else:
                    l = mp + 1

        return -1


        
        

        