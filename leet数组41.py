class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n=len(nums)
        for i in range(n):
            while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                idx=nums[i]-1
                nums[i],nums[idx]=nums[idx],nums[i]
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1
if __name__=="__main__":
    nums=[3,4,-1,1]
    print(Solution().firstMissingPositive(nums))