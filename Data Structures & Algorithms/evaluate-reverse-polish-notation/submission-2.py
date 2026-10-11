class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+","-","*","/"])
        for t in tokens:
            if t in operators:
                b = int(stack.pop())
                a = int(stack.pop())
                if t == "+":
                    stack.append(a+b)
                elif t == "-":
                    stack.append(a-b)
                elif t == "*":
                    stack.append(a*b)
                else:
                    stack.append(a/b)
            else:
                stack.append(t)
        return int(stack[-1])
                
                