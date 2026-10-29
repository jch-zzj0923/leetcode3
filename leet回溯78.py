class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        path=[]
        n=len(nums)
        def dfs(i):
            if i==n:
                ans.append(path.copy())
                return 
            dfs(i+1)
            path.append(nums[i])
            dfs(i+1)
            path.pop()
        dfs(0)
        return ans
if __name__=="__main__":
    nums=[1,2,3]
    s=Solution()
    print(s.subsets(nums))