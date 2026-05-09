class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = nums[0]
        minP, maxP = 0, 0

        for num in nums:
            if num < 0:
                minP, maxP = maxP, minP

            if num == 0:
                minP, maxP = 0, 0
            
            maxP = max(maxP, maxP * num, num)
            minP = min(minP, minP * num, num)
            res = max(res, maxP)
            print(num, minP, maxP)
            print(num, minP, maxP)
            print("///")

        return res