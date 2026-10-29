class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                max_profit = max(max_profit, p - min_price)
        return max_profit
if __name__ == "__main__":
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(prices))  # Output: 5