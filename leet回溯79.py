class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        dire=[(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(i,j,idx):
            if i <0 or i>=m or j<0 or j>=n or board[i][j] != word[idx]:
                return False
            if idx==len(word)-1:
                return True
            temp=board[i][j]
            board[i][j]="#"
            for x,y in dire:
                ni=i+x
                nj=j+y
                if dfs(ni,nj,idx+1):
                    return True 
            board[i][j]=temp
            return False
        for dx in range(m):
            for dy in range(n):
                if dfs(dx,dy,0):
                    return True
        return False        
if __name__ == "__main__":
    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]
    word = "ABCCED"
    solution = Solution()
    result = solution.exist(board, word)
    print(result)  # Output: True