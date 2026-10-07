class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return 0

        jumps = 0
        curr = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == curr:
                jumps += 1
                curr = farthest

                if curr >= len(nums) - 1:
                    break
            
        return jumps
            
