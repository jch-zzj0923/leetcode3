class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res=[]
        if numRows>=1:
            res.append([1])
        if numRows>=2:
            res.append([1,1])
        for i in range(2,numRows):
            tmp=[1]*(i+1)
            for j in range(1,i):
                tmp[j]=res[i-1][j]+res[i-1][j-1]
            res.append(tmp)
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))