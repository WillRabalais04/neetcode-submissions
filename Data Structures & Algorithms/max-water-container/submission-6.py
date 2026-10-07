class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def getArea(i1,i2):
            return min(heights[i1],heights[i2]) * abs(i2-i1)
        m = 0
        l = 0
        r = len(heights) -1   

        while l < r:
            a = getArea(l,r)
            if a > m:
                m = a
            if heights[l] <= heights[r]:
                l += 1
            else: 
                r -= 1

        return m
