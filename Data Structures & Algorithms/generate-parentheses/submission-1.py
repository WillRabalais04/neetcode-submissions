class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ret = []
        def valid(s):
            open = 0
            for c in s:
                open += 1 if c == '(' else -1
                if open < 0:
                    return False
            return not open

        def dfs(s):
            if n * 2 == len(s):
                if valid(s):
                    ret.append(s)
                return
            dfs(s + '(')
            dfs(s + ')')
            return s

        dfs("")
        return ret
        # p = set()

        # def matchParen(rp: List[string]) -> List[str]:
        #     stack = rp
        #     (

        # return p


        # stack = []
        # ()()() 0 
        # (())() 1 
        # ()(()) 2
        # (()()) 3
        # ((())) 4
        

