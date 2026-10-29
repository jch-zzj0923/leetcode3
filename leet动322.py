
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0 
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != INF else -1
if __name__ == "__main__":
    solution = Solution()
    coins = [1, 2, 5]
    amount = 11
    result = solution.coinChange(coins, amount)
    print(result) 