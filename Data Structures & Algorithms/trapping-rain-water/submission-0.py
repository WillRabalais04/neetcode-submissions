class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        heightSum = 0

        lmax = height[l]
        rmax = height[r]

        while l < r: 
            if lmax < rmax:
                l +=1
                lmax = max(lmax, height[l])
                heightSum += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                heightSum += rmax - height[r]
        return heightSum

        

                
