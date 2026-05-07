class Solution:
    def rob(self, nums: List[int]) -> int:
        rob2, rob1 = 0, 0

        for n in nums:
            tmp = max(rob1, rob2 + n)
            rob2 = rob1
            rob1 = tmp
        
        return rob1