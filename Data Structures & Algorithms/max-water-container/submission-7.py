class Solution:
    def maxArea(self, heights: List[int]) -> int:

        if not heights:
            return 0

        l = 0
        r = len(heights) - 1
        maxArea = 0 

        while l < r and l < len(heights) - 1 and r > 0:
            lh = heights[l]
            rh = heights[r]
            w = r - l
            if lh < rh:
                l += 1
            elif lh > rh:
                r -= 1
            else: 
                l += 1
                r -= 1
            area = min(lh,rh) * w
            maxArea = max(maxArea, area)

        return maxArea