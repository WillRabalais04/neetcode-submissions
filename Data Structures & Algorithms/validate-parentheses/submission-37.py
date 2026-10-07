class Solution:
    def isValid(self, s: str) -> bool:
        b = {')': '(', '}': '{', ']':'['}

        stack = []
        for x in s:
            if x not in b:
                stack.append(x)
                continue
            if (not stack or stack[-1] != b[x]):
                 return False
            stack.pop()

        return not stack
            