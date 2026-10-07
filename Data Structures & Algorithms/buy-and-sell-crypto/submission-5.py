class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mp = float("-infinity")

        l,r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                mp = max(mp, (prices[r] - prices[l]))
            else:
                l = r
            r += 1

        return max(mp,0)



        