class Solution:
    def sortColors(self, nums: list[int]) -> None:
        p0 = 0
        p2 = len(nums) - 1
        curr = 0
        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
if __name__ == "__main__":
    sol = Solution()
    nums = [2,0,2,1,1,0]
    sol.sortColors(nums)
    print(nums)