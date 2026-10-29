class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        left=0
        right=len(matrix)-1
        while left<right:
            for i in range(right-left):
                top=left
                bottom=right
                num=matrix[top][left+i]
                matrix[top][left+i]=matrix[bottom-i][left]
                matrix[bottom-i][left]=matrix[bottom][right-i]
                matrix[bottom][right-i]=matrix[top+i][right]
                matrix[top+i][right]=num
            left+=1
            right-=1
if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Solution().rotate(matrix)
    print(matrix)  