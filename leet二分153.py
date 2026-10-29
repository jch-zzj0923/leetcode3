class Solution:
    def findMin(self, nums: list[int]) -> int:
        left=-1
        right=len(nums)-1
        while left+1<right:
            mid=(left+right)//2
            if nums[mid]<nums[-1]:
                right=mid
            else:
                left=mid
        return  nums[right]
if __name__ == "__main__":
    s = Solution()
    print(s.findMin([3,4,5,1,2]))  