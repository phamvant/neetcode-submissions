class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(list(zip(position, speed)), reverse=True)
        stack = []

        for pair in pairs:
            amount = (target - pair[0]) / pair[1]

            if len(stack) and amount > stack[-1]:
                stack.append(amount)
            elif not len(stack):
                stack.append(amount)
            
        return len(stack)
