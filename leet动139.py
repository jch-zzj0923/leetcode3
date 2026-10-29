class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set=set(wordDict)
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(1,n+1):
            for j in range(0,i):
                if dp[j] and s[j:i] in word_set:
                    dp[i]=True
                    break 
        return dp[n]
if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    solution = Solution()
    result = solution.wordBreak(s, wordDict)
    print(result)  # Output: True