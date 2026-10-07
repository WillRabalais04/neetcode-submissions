class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operate(o1, o2, op):
            match op:
                case '+':
                    return o1 + o2
                case '-':
                    return o1 - o2
                case '*':
                    return o1 * o2
                case '/':
                    return int(o1 / o2)
            return -1

        operators = {'+','-','*','/'}
        stack = []

        for t in tokens:
            if t in operators:
                o2 = stack.pop()
                o1 = stack.pop()
                stack.append(operate(o1,o2,t))
            else:
                stack.append(int(t))
            print(stack)

        return stack[0]
            



        