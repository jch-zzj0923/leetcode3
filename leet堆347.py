import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count =Counter(nums)
        head=[]
        for num,freq in count.items():
            heapq.heappush(head,(freq,num ))
            if len(head)>k:
                heapq.heappop(head)
        res=[]
        for item in head:
            freq=item[0]
            num=item[1]
            res.append(num)
        return res 
if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    solution = Solution()
    print(solution.topKFrequent(nums, k))  # Output: [1, 2]