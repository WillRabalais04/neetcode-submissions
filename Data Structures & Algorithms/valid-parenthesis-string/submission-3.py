class Solution:
    def checkValidString(self, s: str) -> bool:

        l_stack = []
        ast_stack = []

        for idx in range(len(s)):
            if s[idx] == '(':
                l_stack.append(idx)
            if s[idx] == '*':
                ast_stack.append(idx)
            if s[idx] == ')':
                if len(l_stack) > 0:
                    l_stack.pop()
                elif len(ast_stack) > 0:
                    ast_stack.pop()
                else:
                    return False

        while len(l_stack) > 0:
            if len(ast_stack) < 1:
                break
            if ast_stack[-1] > l_stack[-1]:
                l_stack.pop()
                ast_stack.pop()
            else:
                return False

        return len(l_stack) == 0





    