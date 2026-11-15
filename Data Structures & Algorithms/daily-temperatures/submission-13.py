class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
    
        for i, t in enumerate(temperatures):
            while len(stack) > 0 and temperatures[stack[-1]] < t:
                idx = stack.pop()
                result[idx] = i - idx

            stack.append(i)

        return result
                    

