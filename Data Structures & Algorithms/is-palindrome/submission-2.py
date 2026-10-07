class Solution:


    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        s_backwards = ""

        i = 0
        while i < len(s):
            char = s[i]
            if not self.isAlphanumeric(char):
                s = s.replace(char, "")
            else:
                i += 1

        for i in range(len(s) - 1, -1 , -1):
            s_backwards += s[i]

        return s == (s_backwards)
    

    def isAlphanumeric(self, c) -> bool:
        return (ord("A") <= ord(c) <= ord("Z")) or (ord("a") <= ord(c) <= ord("z")) or (ord("0") <= ord(c) <= ord("9"))