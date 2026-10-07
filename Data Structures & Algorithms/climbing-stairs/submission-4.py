class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n
        
        ways_per_step = [0] * (n + 1)
        ways_per_step[1], ways_per_step[2] = 1,2
        for i in range(3,n + 1):
            ways_per_step[i] =  ways_per_step[i - 1] + ways_per_step[i - 2]
        return ways_per_step[n]