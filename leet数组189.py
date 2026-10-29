class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        def reverse(arr,left,right):
            while left<right:
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
                right-=1
        n=len(nums)
        k=k%n
        reverse(nums,0,n-1)
        reverse(nums,0,k-1)
        reverse(nums,k,n-1)
        return nums
if __name__=="__main__":
    nums=[1,2,3,4,5,6,7]
    k=3
    solution=Solution()
    print(solution.rotate(nums,k))