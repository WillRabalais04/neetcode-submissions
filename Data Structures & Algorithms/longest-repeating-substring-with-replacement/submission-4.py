class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = r = maxstreak = maxfreq = 0
        freq = [0] * 26

        while r < len(s):
            lidx, ridx = ord(s[l]) - ord('A'), ord(s[r]) - ord('A')
            freq[ridx] += 1
            maxfreq = max(maxfreq, freq[ridx])
            ''' if length of window (r - l) - freq[s[r]] > max num changeable chars (k
                move l right
            '''
            while (r - l + 1) - maxfreq > k:
                freq[lidx] -= 1
                l += 1
            maxstreak = max(maxstreak, r - l + 1)
            r += 1
        return maxstreak

            

