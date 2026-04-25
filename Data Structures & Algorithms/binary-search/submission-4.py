class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r, m = 0, len(nums) - 1, (len(nums) - 1) // 2

        if nums[m] == target:
            return m

        while r > l:
            if nums[m] == target:
                return m

            if nums[l] == target:
                return l

            if nums[r] == target:
                return r
            
            if nums[m] < target:
                l = m
            else: 
                r = m
            
            m  = (l + r) // 2

            if r - l < 2:
                break;

        return -1