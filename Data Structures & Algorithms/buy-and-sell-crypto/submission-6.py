class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0,1
        mp = float("-infinity")
        while r < len(prices):
            profit = prices[r] - prices[l]
            if prices[l] < prices[r]:
                mp = max(mp, profit)
            else:
                l = r
            r += 1
        return max(mp,0)


        