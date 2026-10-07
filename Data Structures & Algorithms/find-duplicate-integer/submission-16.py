class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = fast = 0
        while True: # returns value in a cycle
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True: # circulates 2 values in a cycle so when they are equal you know it's a duplicate
            slow = nums[slow]        
            slow2 = nums[slow2]
            if slow2 == slow:
                return slow
        return -1
