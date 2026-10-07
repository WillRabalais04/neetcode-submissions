class Solution:
    def isValid(self, s: str) -> bool:
        p = {'(':')','{':'}','[':']'}

        stack = []

        for c in s:
            if c in p: 
                stack.append(c)
            elif c in p.values():
                if not stack or p[stack.pop()] != c:
                    return False
                
        
        return len(stack) == 0
