class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]
    
        for i, t in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < t:
                idx, val = stack.pop()
                result[idx] = i - idx

            stack.append((i, t))

        return result
                    

