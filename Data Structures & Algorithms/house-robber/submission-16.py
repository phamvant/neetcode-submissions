class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [None] * (len(nums) + 1)
        self.maxRet = 0

        def dfs(i):
            if i >= len(nums):
                return 0

            if memo[i] is not None:
                return memo[i]
            else:
                tmp = dfs(i + 1)
                tmp2 = nums[i] + dfs(i + 2)
                memo[i] = max(tmp, tmp2)
                return memo[i]

        return dfs(0)