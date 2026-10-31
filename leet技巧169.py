class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([2,2,1,1,1,2,2]))