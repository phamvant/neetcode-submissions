
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            if idx > 0:
                while len(stack) and temp > temperatures[stack[-1]]:
                    res[stack[-1]] = idx - stack[-1]
                    stack.pop()

            stack.append(idx)

        return res