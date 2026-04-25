class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_i = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_i:
                return [num_i[complement], i]
            num_i[num] = i
        