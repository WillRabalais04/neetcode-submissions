class Solution:


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getH(k):
            ret = 0
            for i in range(len(piles)):
                ret += math.ceil(piles[i] / k)
            return ret
        
        l,r = 1, max(piles)
        ret = r

        while l <= r:
            m = (l + r) // 2
            t = getH(m)
            if t <= h:
                ret = m
                r = m - 1
            else:
                l = m + 1
        return ret


        