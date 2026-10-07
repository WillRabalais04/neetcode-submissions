class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ret = []
        def valid(s):
            lpc = 0
            for c in s:
                if lpc < 0:
                    return False
                if c == '(':
                    lpc += 1
                elif c == ')':
                    lpc -= 1
                else:
                    return False
            return not lpc

        def dfs(s):
            if len(s) == n*2:
                if valid(s):
                    ret.append(s)
                return
            dfs(s + '(')
            dfs(s + ')')

        dfs("")
        return ret