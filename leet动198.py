class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        f=[0]*(n+2)
        for i ,x in enumerate(nums):
            f[i+2]=max(f[i+1],f[i]+x)
        return f[n+1]
if __name__ == "__main__":
    s = Solution()
    print(s.rob([1,2,3,1]))  # Output: 4
   