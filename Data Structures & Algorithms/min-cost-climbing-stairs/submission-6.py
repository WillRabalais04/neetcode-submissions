class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        mincost_at_i = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
               return 0
            mincost_at_i[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return mincost_at_i[i]
            
        return min(dfs(0), dfs(1))