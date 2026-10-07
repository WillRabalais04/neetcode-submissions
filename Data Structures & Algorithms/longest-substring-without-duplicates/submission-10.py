class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l,r = 0,0
        streak = 1
        sc = set()
        while r < len(s):
            curr = s[r]
            if not curr in sc:
                r += 1
                sc.add(curr)
                streak = max(streak, r - l)
            else:
                sc.remove(s[l])
                l += 1

        return streak
        