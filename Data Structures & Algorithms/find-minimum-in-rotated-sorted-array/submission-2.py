
class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        minN = 0

        while l <= r:
            m = l + (r - l) // 2

            minN = min(nums[m], nums[r], nums[l])
            if l == r or l == r - 1:
                return minN

            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m
