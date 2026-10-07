class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ret = []
        stack = []

        def backtrack(Lcount,Rcount):
            if Lcount == Rcount == n:
                ret.append("".join(stack))
                return
            if Lcount < n:
                stack.append("(")
                backtrack(Lcount+1,Rcount)
                stack.pop()
            if Rcount < Lcount:
                stack.append(")")
                backtrack(Lcount,Rcount + 1)
                stack.pop()

        backtrack(0,0)
        return ret

        '''
        Input: n = 1
        Output: ["()"]
        Input: n = 2
        Output: ["(())", "()()"]
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]

        (( -> (|(| -> ()()
        (( -> ((|| -> (())
        
        (|||(|||(|||



        ((( ->   (((||| -> ((()))
        ((( ->   ((|(|| -> (()())
        ((( ->   (|((|| -> ()(())
        ((( ->   ((||(| -> (())()
        ((( ->   (|(|(| -> ()()()

        '''

        

        
