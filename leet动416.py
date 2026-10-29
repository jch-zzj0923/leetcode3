class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2 !=0:
            return False
        target=total//2
        dp=[False]*(target+1)
        dp[0]=True
        for  i in nums:
            for j in range(target,i-1,-1):
                dp[j]=dp[j] or dp[j-i]
            if dp[target]:
                return True
        return dp[target] 
if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1, 5, 11, 5]))  # Output: True