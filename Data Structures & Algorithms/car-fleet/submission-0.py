class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        # print(pairs)
        stack = []

        for i in range(len(pairs)):
            movingTime = (target - pairs[i][0]) / pairs[i][1]
            # # print(pairs[i][0], pairs[i][1])
            # print(pairs[i])
            stack.append(movingTime)
            # print(stack)

            # print(movingTime)
            if len(stack) > 1 and movingTime <= stack[len(stack) - 2]:
                # print(movingTime, stack[len(stack) - 1])
                stack.pop()
        
        return len(stack)
