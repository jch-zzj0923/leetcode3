class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=0
        col=len(matrix[0])-1
        while col>=0 and row<len(matrix):
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                row+=1
            elif matrix[row][col]>target:
                col-=1
        return False
if __name__ == "__main__":
    solution = Solution()
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 5
    print(solution.searchMatrix(matrix, target)) 