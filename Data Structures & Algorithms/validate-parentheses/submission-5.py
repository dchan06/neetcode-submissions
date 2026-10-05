class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)): 
            if s[i] == "(" or s[i] == "{" or s[i] == "[": 
                stack.append(s[i])
                continue
            if len(stack) <= 0: 
                return False
            if s[i] == ")" and stack.pop() != "(":
                return False
            if s[i] == "]" and stack.pop() != "[": 
                return False
            if s[i] == "}" and stack.pop() != "{": 
                return False
        if len(stack) == 0: 
            return True
        return False