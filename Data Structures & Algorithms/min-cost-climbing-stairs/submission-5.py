class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        m = [-1] * len(cost)
        def dp(idx):
            if idx >= len(cost):
                return 0
            if m[idx] != -1:
                return m[idx]
            m[idx] = cost[idx] + min(dp(idx + 1), dp(idx + 2))
            return m[idx]
        return min(dp(0), dp(1))


        