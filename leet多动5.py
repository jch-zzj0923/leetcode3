class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<=1:
            return s
        dp=[[False]*n for _ in range(n)]
        max_len=1
        start=0
        for l in range(2,n+1):
            for i in range(n):
                j=i+l-1
                if j>=n:
                    break
                if s[i] != s[j]:
                    dp[i][j]=False
                else:
                    if j-i<=2:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                if l>max_len and dp[i][j]:
                    max_len=l
                    start=i
        return s[start:start+max_len]
if __name__ == "__main__":
    s = "babad"
    solution = Solution()
    print(solution.longestPalindrome(s)) 