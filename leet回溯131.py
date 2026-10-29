class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        path = []
        n = len(s)

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            for j in range(i, n):
                t = s[i:j+1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j + 1)
                    path.pop()
        dfs(0)
        return ans
if __name__ == "__main__":
    s = "aab"
    solution = Solution()
    result = solution.partition(s)
    print(result)  # Output: [["a","a","b"],["aa","b"]]