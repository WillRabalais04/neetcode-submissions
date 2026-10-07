class Solution:
    def climbStairs(self, n: int) -> int:

        def dp(s):
            if s == n:
                return 1
            ret = 0
            if s + 1 <= n:
                ret += dp(s + 1)
            if s + 2 <= n:
                ret += dp(s + 2)
            return ret
        
        return dp(0)
