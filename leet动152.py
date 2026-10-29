class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        pre_max = pre_min = res = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max, pre_min = cur_max, cur_min
        return res
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProduct([2, 3, -2, 4]))  # Output: 6