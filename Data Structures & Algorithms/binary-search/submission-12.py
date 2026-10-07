class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        def binarySearch(nums, target, idxOffset):
            idx = len(nums) // 2

            if not nums:
                return -1
                
            if nums[idx] > target:
                return binarySearch(nums[:idx], target, idxOffset)
            elif nums[idx] < target:
                return binarySearch(nums[idx + 1:], target, (idx + 1) + idxOffset)
            else: 
                return idx + idxOffset
        
        return binarySearch(nums, target, 0)
                
            