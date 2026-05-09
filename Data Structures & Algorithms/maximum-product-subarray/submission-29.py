class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minP, maxP = 1, 1

        for num in nums:
            tmp = maxP * num
            maxP = max(maxP * num, minP * num, num)
            minP = min(minP * num, tmp, num)
            res = max(maxP, res)

        return res