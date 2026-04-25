class Solution:
    def isValid(self, s: str) -> bool:
        bracketPairs = {"]": "[", ")": "(", "}": "{"}

        stack = []

        if len(s) % 2 != 0:
            return False

        for i in range(len(s)):
            if len(stack) > 0 and bracketPairs.get(s[i], 0) == stack[len(stack) - 1]:
                stack.pop()
            else:
                stack.append(s[i])

        if len(stack) == 0:
            return True

        return False