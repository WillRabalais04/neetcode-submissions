class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx,ht = stack.pop()
                c = ht * (i - idx) # pops off stack if elem on top of stack < h and calculates area
                maxArea = max(maxArea,c)
                start = idx
            stack.append((start,h))

        # calculates area of ones that end at the last height
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


        # def getNLeft(h,i):
        #     if i > 0 and heights[i - 1] >= h:
        #         return 1 + getNLeft(h, i - 1)
        #     # elif i == 0:
        #     #     return 1
        #     return 0
        # def getNRight(h,i):

        #     if i < len(heights) - 1 and heights[i + 1] >= h:
        #         return 1 + getNLeft(h, i + 1)
        #     # elif i == len(heights) - 1:
        #         return 1
        #     return 0
        # recSizes = []
        # for i in range(len(heights)):
        #     h = heights[i]
        #     le = getNLeft(h, i)
        #     ri = getNRight(h, i)
        #     w = 1 if (le + ri == 0) else le + ri
        #     print("h: " + str(h) + " | w: " + str(w) + "| l: " + str(le) + " | r: " + str(ri))
        #     recSizes.append(h * w)
        # print(recSizes)
        # return max(recSizes)
        