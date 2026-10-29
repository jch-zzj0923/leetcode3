class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans=[]
        col=[0]*n
        def vilid(r,c):
            for R in range(r):
                C=col[R] 
                if r+c==R+C or r-c==R-C:
                    
                     return False
            return True
        def dfs(r,s):
            if r==n:
                ans.append(["."*c + 'Q' + '.'*(n-1-c) for c in col])
                return
            for c in s:
                if vilid(r,c):
                    col[r]=c
                    dfs(r+1,s-{c})
        dfs(0,set(range(n)))
        return ans
if __name__=="__main__":
    n=4
    s=Solution()
    print(s.solveNQueens(n))