class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Smap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in Smap:
                return [Smap[diff], i]

            Smap[n] = i