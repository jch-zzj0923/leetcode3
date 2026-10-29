class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n=len(nums)
        f=[0]*n
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    f[i]=max(f[j],f[i])
            f[i]+=1
        return max(f)
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))