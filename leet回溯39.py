class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans=[]
        path=[]
        n=len(candidates)
        def dfs(i,cur_sum):
            if cur_sum==target:
                ans.append(path.copy())
                return 
            if cur_sum>target:
                return 
            for j in range(i,n):
                num=candidates[j]
                path.append(num)
                dfs(j,cur_sum+num)
                path.pop()
        dfs(0,0)
        return ans
if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    solution = Solution()
    result = solution.combinationSum(candidates, target)
    print(result)  # Output: [[2, 2, 3], [7]]