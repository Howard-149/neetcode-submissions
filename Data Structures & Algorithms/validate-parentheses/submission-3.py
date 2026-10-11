class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(":")", "{":"}","[":"]" }
        for p in s:
            if p in pairs.keys():
                stack.append(p)
            elif not stack:
                return False
            elif pairs[stack[-1]] == p:
                stack.pop()
            else:
                return False
        if stack == []:
            return True
        else:
            return False