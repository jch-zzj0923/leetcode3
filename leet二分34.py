class Solution:
    def lowre_bound(self,nums:List[int],target:int)->[int]:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start=self.lowre_bound(nums,target)
        if start==len(nums) or nums[start]!=target:
            return [-1,-1]
        end=self.lowre_bound(nums,target+1)-1
        return [start,end]
if __name__=="__main__":
    nums=[5,7,7,8,8,10]
    target=8
    s=Solution()
    print(s.searchRange(nums,target))