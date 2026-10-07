class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ret = []

        def getMaxInWindow(l,r): # O(k) ~ O(1)
            m = float("-infinity")
            for i in range(l,r):
                m = max(m, nums[i])
            return m
        l,r = 0, k

        while r <= len(nums):

            ret.append(getMaxInWindow(l,r))

            l += 1
            r += 1
        
        return ret