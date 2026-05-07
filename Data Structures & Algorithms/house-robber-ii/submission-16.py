class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def solve():
            rob2, rob1 = 0, 0
            start_index = 0

            for i in range(len(nums) - 1):
                index = (start_index + i) % len(nums)
                tmp = max(rob1, rob2 + nums[index])
                rob2 = rob1
                rob1 = tmp
        
            return rob1
        
        def solve2():
            rob2, rob1 = 0, 0
            start_index = 1

            for i in range(len(nums) - 1):
                index = (start_index + i) % len(nums)
                tmp = max(rob1, rob2 + nums[index])
                print(tmp)
                rob2 = rob1
                rob1 = tmp
        
            return rob1
        
        return max(solve(), solve2())