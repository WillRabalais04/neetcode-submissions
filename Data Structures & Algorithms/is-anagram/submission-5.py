class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq = [0] * 26 

        for i in range(len(s)):
            c_s,c_t  = s[i], t[i]
            freq[ord(c_s) - ord('a')] += 1
            freq[ord(c_t) - ord('a')] -= 1
        for v in freq:
            if v != 0:
                return False
        return True

            

        