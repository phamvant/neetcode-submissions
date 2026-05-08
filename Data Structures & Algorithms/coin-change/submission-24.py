class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [None] * (amount + 1)
        
        def solve(amount):
            if amount == 0:
                return 0
            if memo[amount]:
                return memo[amount]
            
            res = 1e9

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + solve(amount - coin))
            
            memo[amount] = res
            return res
        
        ret = solve(amount)

        return ret if ret != 1e9 else -1