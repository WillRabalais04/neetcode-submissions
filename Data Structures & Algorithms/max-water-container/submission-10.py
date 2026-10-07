class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        ret = 0
        l,r = 0, len(heights) - 1

        while l < r:

            area = min(heights[l],heights[r]) * (r-l)
            ret = max(ret, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return ret