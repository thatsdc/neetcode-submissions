class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mem = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s: 
            if c in mem:
                if len(stack) > 0 and mem[c] == stack[-1]:
                    stack.pop();
                else: 
                    return False
            else:
                stack.append(c)

        return not len(stack) > 0
        