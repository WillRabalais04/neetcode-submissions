class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 1
        maxprof = 0

        while r < len(prices):
            prof = prices[r] - prices[l]
            if prof < 0:
                l += 1
            else:
                r +=1
            maxprof = max(maxprof,prof)
        return maxprof


        