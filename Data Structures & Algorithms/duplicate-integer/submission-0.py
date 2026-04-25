class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        if(len(hashmap) != len(nums)):
            return True
        return False