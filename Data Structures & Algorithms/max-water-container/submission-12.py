class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l,r = 0, len(heights) - 1
        ma = 0

        while l < r:
            area = (r - l)
            if heights[l] < heights[r]:
                area *= heights[l]
                l += 1
            else:
                area *= heights[r]
                r -= 1
            ma = max(area, ma)
        return ma
        