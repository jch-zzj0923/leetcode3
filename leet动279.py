class Solution:
    def numSquares(self, n: int) -> int:
        INF = n + 1
        dp = [INF] * (n + 1)
        dp[0] = 0
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
        for s in squares:
            for j in range(s, n + 1):
                dp[j] = min(dp[j], dp[j - s] + 1)
        return dp[n]
if __name__ == "__main__":
    solution = Solution()
    n = 12
    print(solution.numSquares(n))  