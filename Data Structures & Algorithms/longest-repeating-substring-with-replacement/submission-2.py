class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mf,l,ret = 0,0,0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            mf = max(mf, count[s[r]])

            while (r - l + 1) - mf > k:
                count[s[l]] -= 1
                l += 1

            ret = max(ret, (r - l + 1))

        return ret
        

