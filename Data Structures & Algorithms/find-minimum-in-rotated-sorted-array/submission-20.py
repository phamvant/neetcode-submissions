
class Solution:
    def findMin(self, nums: List[int]) -> int:
        ret = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                ret = min(ret, nums[l])
                break

            p = (l + r) // 2
            ret = min(ret, nums[p])
            if nums[p] >= nums[l]:
                l = p + 1
            else:
                r = p - 1
        
        return ret

