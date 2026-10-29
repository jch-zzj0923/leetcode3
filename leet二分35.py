class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left=0
        n=len(nums)
        right=n-1
        n=len(nums)
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left 
if __name__=="__main__":
    nums=[1,3,5,6]
    target=5
    print(Solution().searchInsert(nums,target))