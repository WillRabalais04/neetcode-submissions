class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        q = deque()
        l = r = 0

        while r < len(nums):
            # removes all prev values < nums[r]
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            # remove leftmost value if out of the window
            if q[0] < l:
                q.popleft()
            
            # only print after window reaches size k
            if r + 1 >= k:
                ret.append(nums[q[0]])
                l += 1
            r += 1
        return ret
        