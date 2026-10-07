class Solution:
    def climbStairs(self, n: int) -> int:
        ways_per_step = [-1] * n

        def dfs(step):
            if step >= n:
                return step == n # 1 if at last step vs. 1 0 of past
            if ways_per_step[step] != -1:
                return ways_per_step[step]
            ways_per_step[step] = dfs(step + 1) + dfs(step + 2)
            return ways_per_step[step]
        return dfs(0)
        