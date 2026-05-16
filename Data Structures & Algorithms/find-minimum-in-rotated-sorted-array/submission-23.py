
class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        ret = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                ret = min(ret, nums[l])
                break
                
            p = l + (r - l) // 2
            ret = min(ret, nums[p])
            print(l, r, p)
            if nums[p] >= nums[r]:
                l = p + 1
            else:
                r = p - 1
        
        return ret

