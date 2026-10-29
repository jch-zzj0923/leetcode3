class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if matrix is None:
            return False
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=m*n-1
        while left<=right:
            mid=(left+right)//2
            row=mid//n
            col=mid%n
            val=matrix[row][col]
            if val==target:
                return True
            elif val<target:
                left=mid+1
            else:
                right=mid-1
        return  False
if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    solution = Solution()
    result = solution.searchMatrix(matrix, target)
    print(result)  # Output: True