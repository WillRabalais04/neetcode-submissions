class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")":"(", "}":"{", "]":"["}

        stack = []

        for brace in s:
            if brace not in Map:
                stack.append(brace)
                continue
            if not stack or stack[-1] != Map[brace]:
                return False
            stack.pop()
        
        return not stack

