class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0] * (amount + 1)

        dp[0] = 0

        for i in range(1,amount + 1):
            min_coins = float("inf")
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                min_coins = min(min_coins, dp[diff] + 1)
            dp[i] = min_coins

            
        return dp[amount] if dp[amount] < float("inf") else -1

        