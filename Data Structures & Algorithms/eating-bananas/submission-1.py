class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0

        while l <= r:
            m = l + (r - l) // 2

            sum = 0
            for pile in piles:
                sum += (pile + m - 1) // m
            
            if sum <= h:
                r = m - 1
                if m < res or res == 0:
                    res = m
            elif sum > h:
                l = m + 1
    
        return res
