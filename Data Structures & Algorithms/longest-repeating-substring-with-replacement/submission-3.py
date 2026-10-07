class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxfreq = l = ret = 0
        count = defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1
            maxfreq = max(maxfreq, count[s[r]])
            while (r - l) + 1 - maxfreq > k:
                count[s[l]] -= 1
                l += 1
            ret = max(ret, (r - l) + 1)
        
        return ret
