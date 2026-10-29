class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums)==1:
            return True
        i=0
        cover=0
        n=len(nums)
        while i<=cover:
            cover=max(i+nums[i],cover)
            if cover>=n-1:
                return True
            i+=1
        return False
if __name__ == "__main__":
    nums = [2,3,1,1,4]
    solution = Solution()
    print(solution.canJump(nums))  # Output: True