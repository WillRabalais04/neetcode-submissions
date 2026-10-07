class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        chars_s, chars_t = [0] * 26, [0] * 26 

        for i in range(len(s)):
            c = s[i]
            idx = ord(c) - ord('a')
            chars_s[idx] += 1

        for i in range(len(t)):
            c = t[i]
            idx = ord(c) - ord('a')
            chars_t[idx] += 1
        return chars_s == chars_t
            
            

        