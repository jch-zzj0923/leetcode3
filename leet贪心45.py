class Solution:
    def jump(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        cur=0
        cur_next=0
        retult=0
        for i in range(n):
            cur_next=max(i+nums[i],cur_next)
            if i==cur:
                if cur<n-1:
                    retult+=1
                    cur=cur_next
                    if cur>=n-1:
                        break
        return retult
if __name__ == "__main__":
    s = Solution()
    print(s.jump([2,3,1,1,4]))