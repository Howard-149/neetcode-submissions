class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star_stack = []
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack :
                    stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
            elif c == "*":
                star_stack.append(i)
        while stack:
            if not star_stack:
                return False
            a, b =stack.pop(), star_stack.pop()
            if a>b:
                return False    
        return True
            