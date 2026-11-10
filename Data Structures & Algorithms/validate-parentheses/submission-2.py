class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mem = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s: 
            if len(stack) > 0 and c in mem and mem[c] == stack[-1]:
                stack.pop();
            else:
                stack.append(c)

        return not len(stack) > 0
        