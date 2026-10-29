import heapq
class MedianFinder:
    def __init__(self):
        self.left=[]
        self.right=[]
    def addNum(self, num: int) -> None:
        heapq.heappush(self.left,-num)
        if self.left and self.right and (-self.left[0])>self.right[0]:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        # 平衡数量：左边最多只能比右边多1个
        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        # 右边不能比左边多
        if len(self.right) > len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)
    def findMedian(self) -> float:
        total = len(self.left) + len(self.right)
        if total % 2 == 1:
            # 奇数，左边多一个，中位数是左堆顶
            return -self.left[0]
        else:
            # 偶数，两边平均
            return (-self.left[0] + self.right[0]) / 2
if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # 输出 1.5
    mf.addNum(3)
    print(mf.findMedian())  # 输出 2.0