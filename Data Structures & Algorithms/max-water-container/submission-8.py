class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        mh = 0
        l,r = 0, len(heights) - 1

        while l < r and l < len(heights) and r > 0:
            lh, rh = heights[l], heights[r]
            h = min(lh,rh) * (r - l)
            mh = max(mh, h)

            if lh <= rh:
                l += 1
            else:
                r -= 1

        return mh
