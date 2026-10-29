class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        pre=0
        max_sum=nums[0]
        for i in nums:
            if pre>0:
                pre=pre+i
            else:
                pre=i
            if pre>max_sum:
                max_sum=pre
        return max_sum
if __name__ == "__main__":
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(solution.maxSubArray(nums)) 