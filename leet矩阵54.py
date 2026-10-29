class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res=[]
        left=0
        right=len(matrix[0])-1
        top=0
        bottom=len(matrix)-1
        while top<=bottom and left<=right:
            for j in range(left,right+1):
                res.append(matrix[top][j])
            top+=1
            if top>bottom:
                break
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1
            if left>right:
                break
            for j in range(right,left-1,-1):
                res.append(matrix[bottom][j])
            bottom-=1
            if top>bottom:
                break
            for i in range(bottom,top-1,-1):
                res.append(matrix[i][left])
            left+=1
            if left>right:
                break
        return res
if __name__=="__main__":
    s=Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
   