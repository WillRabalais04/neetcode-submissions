class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ret = []
        q = deque()
        l = r = 0

        # adds elements to end of queue as they are encountered with r

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # if l index > oldest thing on queue index remove it
            if l > q[0]:
                q.popleft()

            # if r index >= k, add max
            if (r + 1) >= k:
                ret.append(nums[q[0]])
                l += 1
            r += 1

        return ret    