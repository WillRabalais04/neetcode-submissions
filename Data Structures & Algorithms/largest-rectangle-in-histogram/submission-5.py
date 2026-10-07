class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        lra = 0
    
        for i,h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                lra = max(lra, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i,h in stack:
            lra = max(lra, h * (len(heights)-i))
        return lra