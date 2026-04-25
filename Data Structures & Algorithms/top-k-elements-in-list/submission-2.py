import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        
        sorted_nums = sorted(count, key=count.get, reverse=True)

        return sorted_nums[:k]