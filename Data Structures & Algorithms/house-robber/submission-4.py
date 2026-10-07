class Solution:
    def rob(self, nums: List[int]) -> int:

        r1, r2 = 0, 0 

        for num in nums:
            temp = max(num + r1, r2)
            print("num: " + str(num) + " | r1: " + str(r1) + " | r2: " + str(r2))
            print(temp)
            r1 = r2
            r2 = temp
        return r2
        