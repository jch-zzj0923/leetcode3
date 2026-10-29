class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        def get_start(x):
            return x[0]
        intervals.sort(key=get_start)
        res=[intervals[0]]
        for cur in intervals[1:]:
            last=res[-1]
            if cur[0]<=last[1]:
                last[1]=max(last[1],cur[1])
            else:
                res.append(cur)
        return res
if __name__=="__main__":
    s=Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
    