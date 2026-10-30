
---

## 70. 爬楼梯
**核心思路**：一维DP，斐波那契递推。走到第i阶，只能从i-1（走1步）或者i-2（走2步）过来，`dp[i] = dp[i-1] + dp[i-2]

1. dp数组：`dp[i]` 代表爬到第i阶的方案数
2. 初始化：`dp[1]=1，dp[2]=2`
3. 从3循环到n，递推计算dp[i]
4. 返回`dp[n]`
```
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        if n >=2:
            dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
```

---

## 118. 杨辉三角

**核心思路**：DP，每行首尾固定是1；中间位置 = 上一行同位置 + 上一行前一个位置
1. 结果列表res保存所有行
2. 边界：numRows=1直接加`[1]`；numRows=2加`[1,1]`
3. i从2开始循环到numRows-1，新建当前行tmp初始全1
4. j遍历中间位置：`tmp[j] = res[i-1][j] + res[i-1][j-1]`
5. 把当前行加入res，最后返回res

```
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
```

---

## 198. 打家劫舍

**核心思路**：一维DP，`f[i]` 前i间房的最大金额；对于第i间，二选一：偷（i-2最优+当前）/不偷（i-1最优)
1. n是房屋数量，dp数组f长度n+2，防止越界
2. 遍历每个房子，x是当前房子钱
3. 状态转移：`f[i+2] = max(f[i+1], f[i]+x)`
4. 返回`f[n+1]`

```
class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        f=[0]*(n+2)
        for i ,x in enumerate(nums):
            f[i+2]=max(f[i+1],f[i]+x)
        return f[n+1]
```

---

## 279. 完全平方数
**核心思路**：完全背包DP。

1. 先预处理所有<=n的完全平方数存入squares
2. dp数组初始化无穷大，`dp[0]=0`（和为0需要0个数）
3. 遍历每一个平方数s
4. j从s遍历到n，更新dp[j]
5. 返回dp[n]

```
class Solution:
    def numSquares(self, n: int) -> int:
        INF = n + 1
        dp = [INF] * (n + 1)
        dp[0] = 0
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
        for s in squares:
            for j in range(s, n + 1):
                dp[j] = min(dp[j], dp[j - s] + 1)
        return dp[n]
```

---

## 322. 零钱兑换
**核心思路**：完全背包
1. INF = amount+1，dp数组初始无穷大，`dp[0]=0`
2. i从1遍历到amount
3. 遍历每一枚硬币coin，如果coin<=i，更新dp[i]
4. 如果dp[amount]仍然是INF返回-1，否则返回dp[amount]

```
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != INF else -1
```

---

## 139. 单词拆分
**核心思路**：DP
1. 把wordDict转集合加速查询，n是字符串长度
2. dp数组全False，`dp[0]=True`（空串合法）
3. i遍历1~n（前i个字符）
4. j遍历0~i，一旦找到满足条件的j，标记dp[i]=True并break
5. 返回dp[n]

```
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set=set(wordDict)
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(1,n+1):
            for j in range(0,i):
                if dp[j] and s[j:i] in word_set:
                    dp[i]=True
                    break
        return dp[n]
```

---

## 300. 最长递增子序列 LIS

**核心思路**：朴素DP
1. n=数组长度，f数组初始全部为1（每个元素自身长度是1）
2. i逐个遍历每个位置
3. j遍历i前面所有元素，满足大小关系就更新f[i]
4. 返回f数组最大值

```
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n=len(nums)
        f=[0]*n
        for i in range(n):
            f[i]=1
            for j in range(i):
                if nums[j]<nums[i]:
                    f[i]=max(f[j]+1,f[i])
        return max(f)
```

---

## 152. 乘积最大子数组
**核心思路**：DP，同时保存以当前位置结尾的最大值、最小值；遇到负数交换最大最小
1. pre_max、pre_min、res初始化为nums[0]
2. 从第二个数开始遍历
3. 计算当前cur_max、cur_min
4. 更新全局最大值res
5. 更新pre_max、pre_min为当前值，继续循环
6. 返回res
```
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        pre_max = pre_min = res = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max, pre_min = cur_max, cur_min
        return res
```

---

## 416. 分割等和子集）
**核心思路**：01背包，物品只能选一次
1. 总和total，如果奇数直接False；target=total//2
2. dp数组False，`dp[0]=True`
3. 遍历每一个数字i
4. j从target倒序遍历到i，更新dp[j]
5. 中途dp[target]为True可以提前返回；最后返回dp[target]

```
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total=sum(nums)
        if total%2!=0:
            return False
        target=total//2
        dp=[False]*(target+1)
        dp[0]=True
        for i in nums:
            for j in range(target,i-1,-1):
                dp[j]=dp[j] or dp[j-i]
                if dp[target]:
                    return True
        return dp[target]
```

---

## 32. 最长有效括号
**核心思路**：DP
- s[i]是`(`：dp[i]=0
- s[i]是`)`：
  - s[i-1] = `(` → `dp[i] = dp[i-2] + 2`
  - s[i-1] = `)`：跳过去看i-dp[i-1]-1位置，如果是`(`，`dp[i] = dp[i-1]+2 + dp[i-dp[i-1]-2]`
1. n字符串长度，dp数组全0，max_len记录答案
2. i从1遍历到n-1
3. s[i]是右括号，分两种情况转移dp[i]
4. 每次更新max_len
5. 返回max_len

```
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n=len(s)
        dp=[0]*n
        max_len=0
        for i in range(1,n):
            if s[i]==')':
                if s[i-1]=='(':
                    dp[i]=dp[i-2]+2 if i>2 else 2
                else:
                    m=i-dp[i-1]-1
                    if m>=0 and s[m]=='(':
                        dp[i]=2+dp[i-1]
                        if m-1>=0:
                            dp[i]+=dp[m-1]
                max_len=max(max_len,dp[i])
        return max_len
```

---


---
## 62. 不同路径
**核心思路**：二维DP。`dp[i][j]` 代表走到坐标`(i,j)`的路径总数。

1. 创建m行n列dp二维数组，全部初始0
2. 把第0列所有格子置1，第0行所有格子置1
3. 遍历i从1~m-1，j从1~n-1，按转移公式填表
4. 返回右下角`dp[m-1][n-1]`

```
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
```

---
## 64. 最小路径和
**核心思路**：二维DP。
1. 获取网格行数m、列数n，构造dp数组
2. 初始化起点`dp[0][0]=grid[0][0]`
3. 填充第0列：只能从上往下走
4. 填充第0行：只能从左往右走
5. 双重循环填充其余位置，取左、上最小值+当前值
6. 返回右下角`dp[m-1][n-1]`

```
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=grid[0][0]
        for i in range(1,m):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for j in range(1,n):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
        return dp[m-1][n-1]
```

---
## 5. 最长回文子串
**核心思路**：二维DP。
1. n为字符串长度，n<=1直接返回原串
2. 初始化n×n布尔dp数组，记录最长长度max_len、起始位置start
3. 枚举子串长度l从2到n
4. 枚举左端点i，算出右端点`j=i+l-1`
5. 判断`s[i]`与`s[j]`：不相等则dp[i][j]=False；相等：
   - 长度<=2：直接为True
   - 更长：依赖内层`dp[i+1][j-1]`
6. 如果是回文，更新最长长度和起点
7. 截取并返回子串


```
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<=1:
            return s
        dp=[[False]*n for _ in range(n)]
        max_len=1
        start=0
        for l in range(2,n+1):
            for i in range(n):
                j=i+l-1
                if j>=n:
                    break
                if s[i]!=s[j]:
                    dp[i][j]=False
                else:
                    if j-i<2:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                if l>max_len and dp[i][j]:
                    max_len=l
                    start=i
        return s[start:start+max_len]
```

---
## 1143. 最长公共子序列 LCS
**核心思路**：二维DP。
1. m、n分别为两个字符串长度，构建`(m+1)*(n+1)`dp表（空串作为第0行第0列）
2. i从1到m遍历text1，j从1到n遍历text2
3. 字符相等：左上角值+1；不等：取上、左最大值
4. 最后`dp[m][n]`就是答案

```
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[m][n]
```

---
## 72. 编辑距离
**核心思路**：二维DP。
  - 删除word1字符：`dp[i-1][j]+1`
  - 插入word1字符：`dp[i][j-1]+1`
  - 替换字符：`dp[i-1][j-1]+1`
1. m、n为两个单词长度，`(m+1)*(n+1)`dp表
2. 初始化第0行：空word1，不断插入，dp[0][j]=j
3. 初始化第0列：空word2，不断删除，dp[i][0]=i
4. 双重循环填表：字符相等取左上角；不等取三者最小值+1
5. 返回`dp[m][n]`

```
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=i
        for j in range(n+1):
            dp[0][j]=j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
        return dp[m][n]
```

---
