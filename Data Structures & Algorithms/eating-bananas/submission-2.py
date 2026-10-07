class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r = 1, max(piles)
        minK = r

        def time(k):
            t = 0
            for p in piles:
                t += math.ceil(p / k)
            return t

        while l <= r:
            m = (l + r) // 2
            if time(m) > h:
                l = m + 1
            else: 
                r = m - 1
                minK = min(minK, m)
        return minK

