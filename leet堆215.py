import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            heapq.heappush(heap, x)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    print(sol.findKthLargest(nums, k))  