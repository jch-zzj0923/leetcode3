Num=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        n=len(digits)
        if n==0:
            return []
        res=[]
        path=[''] * n
        def dfs(i):
            if i==n:
                res.append(''.join(path))
                return 
            for c in Num[int(digits[i])]:
                path[i]=c
                dfs(i+1)
        dfs(0)
        return res
if __name__ == "__main__":
    digits = "23"
    solution = Solution()
    result = solution.letterCombinations(digits)
    print(result) 