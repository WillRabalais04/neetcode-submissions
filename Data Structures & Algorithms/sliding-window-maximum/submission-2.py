class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ret = []
        q = deque()
        l = r = 0

        # adds elements to end of queue is smaller than smallest (rightmost)

        while r < len(nums):
            # removes from right side if nums[r] is greater
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # removes largest val if outside window
            if l > q[0]:
                q.popleft()

            # only appends to ret after window is >= size k
            if (r + 1) >= k:
                ret.append(nums[q[0]])
                l += 1
            r += 1

        return ret    