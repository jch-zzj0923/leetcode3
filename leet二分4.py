class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        left=0
        right=m
        half=(m+n+1)//2
        while left<right:
            i=(left+right+1)//2
            j=half-i
            if  nums1[i-1]>nums2[j]:
                right-=1
            else:
                left+=1
        i=left
        j=half-i 
        nums1_left=nums1[i-1] if i>0 else float('-inf')
        nums1_right=nums1[i] if i<m else float('inf')
        nums2_left=nums2[j-1] if j>0 else float('-inf')
        nums2_right=nums2[j] if j<n else float('inf')
        max_left=max(nums1_left,nums2_left)
        min_right=min(nums1_right,nums2_right)
        if (m+n)%2==1:
            return max_left
        else:
            return (max_left+min_right)/2
if __name__=="__main__":
    nums1=[1,2]
    nums2=[3,4]
    solution=Solution()
    print(solution.findMedianSortedArrays(nums1,nums2))