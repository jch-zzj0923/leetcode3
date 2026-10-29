class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n=len(s)
        dp=[0]*n
        max_len=0
        for i in range(1,n):
            if s[i]==')':
                if  s[i-1]=='(' :
                    dp[i]=dp[i-2]+2 if i>2 else 2
                else:
                    m=i-dp[i-1]-1                  
                    if m>=0 and s[m]=='(':
                        dp[i]=2+dp[i-1]
                        if m-1>0:
                            dp[i]+=dp[m-1]
                max_len=max(max_len,dp[i])
        return max_len            
if __name__=="__main__":
    s = Solution()
    print(s.longestValidParentheses(")()())")) 