class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # dist from goal
        dfg : int = 0
        for i in range(len(nums)-1,-1, -1):
            print(f"i: {i} nums[i]: {nums[i]} dfg: {dfg}")
            if nums[i] >= dfg:
                print("!!!")
                dfg = 0
            if i > 0:
                dfg += 1


        return dfg < 1

        