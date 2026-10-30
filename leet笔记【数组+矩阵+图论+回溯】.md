
## 53. 最大子数组和｜中等
**核心思路**：贪心DP
`pre` 代表以当前元素结尾的最大子数组和。
如果前面的和 `pre>0`，对当前元素有益，接上；否则抛弃前面，从当前数字重新开始。同步更新全局最大 `max_sum`。

1. 初始化 `pre=0`，`max_sum = nums[0]`
2. 遍历每一个数字 `i`：
   - `pre>0`：`pre += i`
   - 否则：`pre = i`
   - 更新 `max_sum = max(max_sum, pre)`
3. 返回 `max_sum`

```python
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        pre=0
        max_sum=nums[0]
        for i in nums:
            if pre>0:
                pre=pre+i
            else:
                pre=i
            if pre>max_sum:
                max_sum=pre
        return max_sum
```

---

## 56. 合并区间｜中等
**核心思路**：贪心，先按区间起点排序，依次和结果最后一个区间比较，重叠就合并，不重叠直接追加。

1. 定义取起点的排序key，对区间排序
2. 结果列表先存入第一个区间
3. 遍历剩下区间：
   - 当前区间起点 ≤ 结果最后区间终点 → 合并，更新终点
   - 否则直接加入结果
4. 返回结果

```python
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
```

---

## 189. 轮转数组｜中等
 **核心思路**：三次原地反转
整体反转 → 前k个反转 → 后面n-k个反转，实现向右轮转。先取模 `k%n` 避免k超过数组长度。


1. 写reverse辅助函数，反转下标left~right
2. n=len(nums), k = k % n
3. reverse(0, n-1)
4. reverse(0, k-1)
5. reverse(k, n-1)
```python
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        def reverse(arr,left,right):
            while left<right:
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
                right-=1
        n=len(nums)
        k=k%n
        reverse(nums,0,n-1)
        reverse(nums,0,k-1)
        reverse(nums,k,n-1)
```

---

## 238. 除自身以外数组的乘积｜中等
 **核心思路**：前缀积 × 后缀积
res先存左边所有数乘积；再从右往左遍历，乘上右侧乘积。


1. n=len(nums)，res初始全1
2. 从左向右：`res[i] = res[i-1] * nums[i-1]`，记录前缀积
3. right=1，从右向左：`res[i] *= right`，更新right
4. 返回res

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n 
        for i in range(1,n):
            res[i]=res[i-1]*nums[i-1]
        right=1
        for i  in range(n-1,-1,-1):
            res[i]=res[i]*right
            right=right*nums[i]
        return res
```

---

## 41. 缺失的第一个正数｜困难
 **核心思路**：原地哈希（桶排序）
数字x应该放到下标 `x-1` 的位置。交换归位后，遍历找第一个 `nums[i] != i+1`，答案就是i+1。全部合法返回n+1。


1. 遍历每个i：while循环，把1~n之间的数字放到正确下标
2. 再次遍历，找到第一个不满足 `nums[i]==i+1` 的位置
3. 返回i+1；全部符合返回n+1

```python
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n=len(nums)
        for i in range(n):
            while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                idx=nums[i]-1
                nums[i],nums[idx]=nums[idx],nums[i]
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1

```

---

## 73. 矩阵置零｜中等
 **核心思路**：用**第一行、第一列做标记**，先单独记录第一行、第一列本身是否含0，再打标记、置零，最后处理首行首列。


1. 提前标记row0、col0：第一行/第一列有没有0
2. 遍历i>=1,j>=1：遇到0，把同行首、同列首置0
3. 遍历i>=1,j>=1：行首或列首为0，当前格子置0
4. 根据row0、col0处理第一行、第一列

```python
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        row0=False
        col0=False
        for j in range(n):
            if matrix[0][j]==0:
                row0=True 
                break
        for i in range(m):
            if matrix[i][0]==0:
                col0=True
                break
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if row0:
            for j in range(n):
                matrix[0][j]=0
        if col0:
            for i in range(m):
                matrix[i][0]=0
```

---

## 54. 螺旋矩阵｜中等
 **核心思路**：边界收缩模拟，按 右→下→左→上 顺序遍历。


1. 初始化 top,bottom,left,right 四个边界
2. 循环：
   - 左→右遍历top行，top+=1，判断退出
   - 上→下遍历right列，right-=1，判断退出
   - 右→左遍历bottom行，bottom-=1，判断退出
   - 下→上遍历left列，left+=1，判断退出
3. 返回结果列表

```python
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

```

---

## 48. 旋转图像｜中等（你的分层旋转写法）
 **核心思路**：分层原地旋转正方形，一圈一圈交换四个对应位置元素

1. left、right标记当前层左右边界
2. 每层循环：依次交换四个角对应位置
3. left += 1，right -=1，向内收缩，直到 left >= right

```python
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
```

---

## 240. 搜索二维矩阵 II｜中等
**核心思路**：Z字形查找，起点选右上角。右上角是本行最大、本列最小。
target更大：往下一行；target更小：往左一列。


1. row=0，col = 最后一列下标（右上角）
2. 循环，不越界：
   - 相等 → True
   - 当前值 < target → row += 1
   - 当前值 > target → col -=1
3. 出循环返回False

```python
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
```


---
## 200. 岛屿数量（DFS 深度优先搜索）
 核心思路：
遍历网格，遇到陆地`"1"`，岛屿数量+1，然后**DFS把这块连通陆地全部标记为水`"0"`（原地访问标记，省去visited数组）**，四个方向上下左右递归。
> 连通块计数模板（无向图连通分量）

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        count = 0
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            grid[i][j] = '0'  # 标记已访问
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count
```
---
## 994. 腐烂的橘子（BFS 广度优先搜索）
 核心思路：
BFS天然适合**层序扩散、求最短时间**。
1. 先遍历网格：把所有一开始腐烂橘子`2`入队；同时统计新鲜橘子总数`fresh`
2. 每一轮while循环，一次性处理当前队列里**这一层所有腐烂橘子**（代表1分钟），把相邻新鲜橘子腐蚀，新鲜橘子数减少，新腐烂的入队
3. 最后：如果新鲜橘子>0 → 返回-1；否则返回用时time
```python
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        fresh = 0
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        time = 0
        while q and fresh > 0:
            sz = len(q)
            for _ in range(sz):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))
            time += 1
        return time if fresh == 0 else -1
```
---
## 207. 课程表（拓扑排序，有向图判环）
核心思路：
课程依赖 = **有向图**（`[a,b]`：b → a，先学b才能学a）
拓扑排序（Kahn算法）：
1. 建邻接表 + 入度数组 `in_degree`
2. 入度为0的节点先入队（没有前置课）
3. 不断弹出队首，把它指向的后继节点入度-1；后继入度变成0就入队
4. 统计一共能取出多少节点；如果取出数量 == 总课程数 → 无环，可以学完；否则有环，返回False

```python
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)   # b -> a 学a需要先学b
            in_degree[a] += 1
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        cnt = 0
        while q:
            cur = q.popleft()
            cnt += 1
            for nxt in graph[cur]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    q.append(nxt)
        return cnt == numCourses
```

---
## 208. 实现Trie（前缀树 / 字典树）
 核心思路：
Trie节点：`children`字典（字符映射子节点） + `is_end`标记（是不是一个单词的结尾）
三个接口：
- insert：逐个字符往下走，不存在就新建节点，最后标记is_end=True
- search：走完所有字符，**并且最后节点is_end=True**，才是完整单词
- startsWith：走完所有字符即可，不需要is_end

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return True
```

---

## 78. 子集

### 核心思路
按顺序枚举每个元素，**每个元素二选一：选 / 不选**。
因为不要求顺序、元素无重复，为避免重复子集，按索引顺序往后搜，不能回头选前面元素。

1. dfs参数i：当前处理下标
2. 递归终点：`i == n`，把当前path拷贝加入答案，返回
3. 分支1：不选nums[i] → 直接dfs(i+1)
4. 分支2：选nums[i] → path.append，dfs(i+1)，递归回来pop()回溯

```python
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        path = []
        n = len(nums)
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            dfs(i+1)
            path.append(nums[i])
            dfs(i+1)
            path.pop()
        dfs(0)
        return ans
```

---

## 46. 全排列
### 核心思路
排列关心顺序，每个位置放一个没使用过的数字；用集合记录还剩哪些数字可以选。
依次填充path的第i个位置，选一个未使用数字放进去，递归填下一位，回溯。
1. dfs(i)：填充path第i个位置，s是剩余可选数字集合
2. 终点：`i == n`，保存path
3. 遍历s里每一个数字x：放到path[i]，dfs(i+1, s-{x})，自动回溯（集合传参，不用pop）
### 代码
```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        path = [0]*n
        def dfs(i, s):
            if i == n:
                ans.append(path.copy())
                return
            for x in s:
                path[i] = x
                dfs(i+1, s-{x})
        dfs(0, set(nums))
        return ans
```


---

## 17. 电话号码的字母组合

### 核心思路
按数字顺序，逐个位置选对应数字下的一个字母填充path；本质是**多叉树枚举**。

1. 建立数字-字母映射表
2. dfs(i)：处理digits第i位
3. 终点：`i == n`，path拼接字符串加入答案
4. 遍历当前数字对应的每一个字母，填入path[i]，递归i+1
### 代码
```python
Num = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        n = len(digits)
        if n == 0:
            return []
        res = []
        path = [""] * n
        def dfs(i):
            if i == n:
                res.append("".join(path))
                return
            for c in Num[int(digits[i])]:
                path[i] = c
                dfs(i+1)
        dfs(0)
        return res
```

---

## 39. 组合总和

### 核心思路
组合不考虑顺序、可重复选同一个数；为防止`[2,3] [3,2]`重复，**只能从当前下标j往后选，不回头**。
cur_sum记录当前和，超过target直接剪枝。
1. dfs(i, cur_sum)：从i下标开始选，当前累加和cur_sum
2. 终点：cur_sum == target → 收集path；cur_sum>target直接return剪枝
3. j从i开始遍历候选：加入path，dfs(j, cur_sum+num)（还能再选自己），回溯pop
### 代码
```python
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        path = []
        n = len(candidates)
        def dfs(i, cur_sum):
            if cur_sum == target:
                ans.append(path.copy())
                return
            if cur_sum > target:
                return
            for j in range(i, n):
                num = candidates[j]
                path.append(num)
                dfs(j, cur_sum + num)
                path.pop()
        dfs(0, 0)
        return ans
```

---

## 22. 括号生成

### 核心思路
合法规则：任意前缀，左括号数量 ≥ 右括号；总左、右都等于n。
dfs填充path第i位，用open记录已经放了多少左括号。

1. dfs(i, open)：填第i个位置，open=已用左括号数
2. 终点：i == 2n，收集字符串
3. 分支1：左括号没放满n个，可以放'('，open+1
4. 分支2：已放左括号 > 已放右括号，可以放')'
### 代码
```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        m = n * 2
        ans = []
        path = [""] * m
        def dfs(i, open):
            if i == m:
                ans.append("".join(path))
                return
            # 放左括号：左括号总数不超过n
            if open < n:
                path[i] = '('
                dfs(i+1, open+1)
            # 放右括号：右括号数量 < 左括号
            if i - open < open:
                path[i] = ')'
                dfs(i+1, open)
        dfs(0, 0)
        return ans
```


---

## 79. 单词搜索

### 核心思路
网格回溯：从每个起点出发，往四个方向深度搜索；走过的格子临时标记为#防止回头，递归结束恢复（原地回溯）

1. dfs(i,j,idx)：当前坐标(i,j)，匹配到单词第idx位
2. 越界 or 字符不匹配 → False；idx走到末尾，匹配成功返回True
3. 保存当前格子字符，改成#标记已访问
4. 四个方向递归，有一条通路为True就返回True
5. 恢复格子字符（回溯）
6. 遍历网格每一个点作为起点搜索
### 代码
```python
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dire = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(i,j,idx):
            # 越界或者字符不对
            if i < 0 or i >= m or j <0 or j >=n or board[i][j] != word[idx]:
                return False
            # 全部匹配完成
            if idx == len(word)-1:
                return True
            temp = board[i][j]
            board[i][j] = '#' # 标记走过
            for dx, dy in dire:
                ni, nj = i+dx, j+dy
                if dfs(ni, nj, idx+1):
                    return True
            board[i][j] = temp # 回溯恢复
            return False
        for dx in range(m):
            for dy in range(n):
                if dfs(dx, dy, 0):
                    return True
        return False
```

---

## 131. 分割回文串

### 核心思路
从i位置开始，枚举结束位置j，截取子串s[i:j+1]，判断是否回文；是回文就选它加入path，继续dfs(j+1)，回溯。

1. dfs(i)：从下标i开始分割
2. i == n：分割完成，收集path
3. j从i到n-1：截取t = s[i:j+1]
4. 如果t是回文串，加入path，dfs(j+1)，递归后pop回溯
### 代码
```python
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        path = []
        n = len(s)
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            # j是分割终点
            for j in range(i, n):
                t = s[i:j+1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return ans
```

---

## 51. N皇后

### 核心思路
按行放置（一行只放一个皇后，天然满足不同行）；col数组记录第r行皇后放在第几列；
放之前校验：和前面所有行皇后是否同列 / 同对角线（r+c相等 或者 r-c相等）

1. dfs(r, s)：r是当前行，s是还能选的列集合
2. r == n：构造棋盘字符串存入答案
3. 遍历可选列c：校验合法，记录col[r]=c，dfs(r+1, s-{c})，回溯
### 代码
```python
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        col = [0]*n
        def valid(r, c):
            # 检查0~r-1行
            for R in range(r):
                C = col[R]
                if r+c == R+C or r - c == R - C:
                    return False
            return True
        def dfs(r, s):
            if r == n:
                ans.append(["."*c + 'Q' + '.'*(n-1-c) for c in col])
                return
            for c in s:
                if valid(r, c):
                    col[r] = c
                    dfs(r+1, s - {c})
        dfs(0, set(range(n)))
        return ans
```

---



