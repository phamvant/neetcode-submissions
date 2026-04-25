class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        # print(pairs)
        prevTime = 0 
        res = 0

        for i in range(len(pairs)):
            movingTime = (target - pairs[i][0]) / pairs[i][1]
            # print(movingTime, prevTime)
            res += 1

            if movingTime <= prevTime:
                res -= 1
            else:
                prevTime = movingTime
        
        return res