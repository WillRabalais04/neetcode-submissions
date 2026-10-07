class Solution:
    def isPalindrome(self, s: str) -> bool:

        x = ""
        for i in range(len(s)):
            if s[i].isalnum():
                x += (s[i].lower())
        print(x)
        for i in range(len(x)):
            print("i: " + str(i) + " x[i]: " + str(x[i]) + " | x[-i]: " + str(x[-i]))
            if x[i] != x[len(x) - 1 -i]:
                return False
        return True
        