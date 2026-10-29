from typing import List
from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])  
        q=deque()
        flash=0
        dirs=[(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    flash+=1
        time=0
        while q and flash>0:
            len_size=len(q)
            for _ in range(len_size):
                x,y=q.popleft()
                for dx,dy in dirs:
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        flash-=1
                        q.append((nx,ny))
            time+=1
        return time if flash==0 else -1
if __name__=="__main__":
    grid=[[2,1,1],[1,1,0],[0,1,1]]
    s=Solution()
    print(s.orangesRotting(grid))