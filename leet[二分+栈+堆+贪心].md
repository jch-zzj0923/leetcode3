
## 35. 搜索插入位置

### 核心思路

有序无重复升序数组，二分查找；找到target返回下标；找不到，`left` 天然就是插入位置（lower_bound）。

1. 初始化 `left=0, right=len(nums)-1`
2. `while left <= right` 计算mid
3. `nums[mid]==target`：直接return mid
4. `nums[mid]<target`：目标在右侧 → `left=mid+1`
5. 否则：目标在左侧 → `right=mid-1`
6. 循环结束，返回left

```
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left=0
        n=len(nums)
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left
```
---

## 74. 搜索二维矩阵

### 核心思路

矩阵**每行升序、上一行最后一个 < 下一行第一个**，可以把二维数组**扁平化当成一维有序数组二分**，一维下标映射回 `row, col`。

1. m行n列，一维总长度 `m*n`，`left=0, right=m*n-1`
2. while `left <= right`，mid是一维索引
3. 映射：`row = mid // n`，`col = mid % n`
4. 取出 `val = matrix[row][col]`
5. val == target → True；val < target → left=mid+1；else → right=mid-1
6. 找不到返回False

```
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
        return False
```

---

## 34. 在排序数组中查找元素的第一个和最后一个位置

### 核心思路
- 起始位置 = lower_bound(nums, target)
- 结束位置 = lower_bound(nums, target+1) - 1
1. 写内部函数 `lower_bound`，返回第一个≥x的下标
2. start = lower_bound(nums, target)
3. 校验：start越界 或者 nums[start]≠target → [-1,-1]
4. end = lower_bound(nums, target+1) - 1
5. 返回 [start, end]

```
class Solution:
    def lower_bound(self,nums:list[int],target:int)->int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start=self.lower_bound(nums,target)
        if start==len(nums) or nums[start]!=target:
            return [-1,-1]
        end=self.lower_bound(nums,target+1)-1
        return [start,end]
```
---

## 33. 搜索旋转排序数组

### 核心思路
二分先判断哪边有序，再看target在不在有序区间里，决定收缩哪边。

1. left=0, right=len(nums)-1
2. while left<=right，mid=(left+right)//2
3. nums[mid]==target → return mid
4. 判断**左半段有序** `nums[left] <= nums[mid]`
   - 如果target落在 `[nums[left], nums[mid]]`：去左边搜 `right=mid-1`
   - 否则去右边搜 `left=mid+1`
5. 否则**右半段有序**
   - 如果target落在 `[nums[mid], nums[right]]`：去右边搜 `left=mid+1`
   - 否则去左边搜 `right=mid-1`
6. 循环结束没找到返回-1

```
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]:
                # 左半边有序
                if nums[left]<=target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                # 右半边有序
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
```
---

## 153. 寻找旋转排序数组中的最小值

### 核心思路
旋转升序无重复数组，最小值就是**旋转断点**；采用 `left+1 < right` 循环

1. left=-1，right=len(nums)-1
2. while `left+1 < right`：mid=(left+right)//2
3. 如果 `nums[mid] < nums[-1]`：最小值在mid及左边 → right=mid
4. 否则：最小值在mid右边 → left=mid
5. 最后返回 nums[right]

```
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left=-1
        right=len(nums)-1
        while left+1<right:
            mid=(left+right)//2
            if nums[mid]<nums[-1]:
                right=mid
            else:
                left=mid
        return nums[right]
```
---

## 4. 寻找两个正序数组的中位数
### 核心思路
对短数组做二分切割，找到分割线，满足：左半边全部 ≤ 右半边；根据总长度奇偶算中位数。要求 O(log(min(m,n)))
1. 保证nums1是更短的数组（交换，减少二分次数）
2. m=len(nums1), n=len(nums2)；left=0, right=m，half=(m+n+1)//2
3. while left<right：i=(left+right+1)//2（nums1分割点），j=half-i（nums2分割点）
4. 比较 `nums1[i-1] > nums2[j]` → 分割线太靠右，right=i-1；否则left=i
5. 拿到最终分割i、j，处理边界（i=0/i=m/j=0/j=n，用正负无穷）
6. 拿到左最大max_left、右最小min_right
7. 总长度奇数：中位数=max_left；偶数：(max_left+min_right)/2
```
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        left=0
        right=m
        half=(m+n+1)//2
        while left<right:
            i=(left+right+1)//2
            j=half-i
            if nums1[i-1]>nums2[j]:
                right=i-1
            else:
                left=i
        i=left
        j=half-i
        nums1_left=nums1[i-1] if i>0 else float('-inf')
        nums1_right=nums1[i] if i<m else float('inf')
        nums2_left=nums2[j-1] if j>0 else float('-inf')
        nums2_right=nums2[j] if j<n else float('inf')
        max_left=max(nums1_left,nums2_left)
        min_right=min(nums1_right,nums2_right)
        if (m+n)%2==1:
            return max_left
        else:
            return (max_left+min_right)/2
```
---

## 20. 有效的括号

### 核心思路

遇到左括号入栈；遇到右括号，弹出栈顶，校验是否匹配。
最后栈为空说明全部匹配成功；匹配失败、栈空还要弹出，直接返回False。

### 简略步骤

1. 初始化空栈
2. 遍历字符串每个字符：
   - 左括号 `( { [` → 压入栈
   - 右括号：栈为空 或者 栈顶和当前右括号不匹配 → 返回False
3. 遍历结束，返回**栈长度是否为0**


```
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                st.append(i)
            elif i == ')':
                if not st or st.pop() != '(':
                    return False
            elif i == '}':
                if not st or st.pop() != '{':
                    return False
            elif i == ']':
                if not st or st.pop() != '[':
                    return False
        return len(st) == 0
```

---

## 155. 最小栈

### 核心思路

**双栈设计**：主栈存所有元素；最小栈同步存到当前位置为止的最小值，保证 `getMin()` O(1) 获取最小值。

1. 构造函数：初始化主栈`stack`、最小值栈`min_stack`
2. push：主栈加入value；最小栈为空就直接加，否则加入`min(value, min_stack[-1])`
3. pop：两个栈同时弹出栈顶
4. top：返回主栈栈顶
5. getMin：返回最小栈栈顶

```
class MinStack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(min(value,self.min_stack[-1]))
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min_stack[-1]
```

---

## 394. 字符串解码

### 核心思路

嵌套结构

1. 初始化空栈，遍历字符串每一个字符
2. 字符不是`]`：直接压栈
3. 遇到`]`：
   - 不断弹出，拼接出括号内的子串`cur`，直到碰到`[`，把`[`弹出
   - 继续弹出，取出前面的数字k（可能多位数）
   - 子串重复k次，逐个字符压回栈
4. 遍历结束，栈内字符拼接为答案
```
class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        n = len(s)
        for i in range(n):
            ch = s[i]
            if ch != ']':
                st.append(ch)
            else:
                cur = ""
                while st[-1] != '[':
                    cur = st.pop() + cur
                st.pop()
                k = ""
                while st and st[-1].isdigit():
                    k = st.pop() + k
                cur = cur * int(k)
                for c in cur:
                    st.append(c)
        return "".join(st)
```

---

## 739. 每日温度

### 核心思路
**单调递减栈**，栈里面存温度下标。栈中下标对应的温度保持递减；当遍历到温度大于栈顶温度，说明找到了栈下标的「下一个更高温」，弹出栈顶计算天数差。

1. 答案数组ans初始全0，空栈st
2. 枚举下标i、温度t：
   - 循环：栈不为空，且当前温度 > 栈下标对应的温度
     - 弹出栈顶下标j
     - ans[j] = i - j
   - 当前下标i入栈
3. 返回ans

```
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        ans=[0]*n
        st=[]
        for i, t in enumerate(temperatures):
            while st and t > temperatures[st[-1]]:
                j=st.pop()
                ans[j]= i-j
            st.append(i)
        return ans
```
---

## 84. 柱状图中最大的矩形

### 核心思路

- 栈顶是它**左边第一个比它小的柱子下标**
- 当前i是它**右边第一个比它小的柱子下标**
宽度 = 右边界 - 左边界 - 1，面积=高度×宽度，更新最大值。
末尾追加0，强制把栈内剩余元素全部结算。

1. 栈st空，max_size=0；heights末尾append(0)作为哨兵
2. 枚举下标l、高度h：
   - 循环：栈不为空，h < heights[st[-1]]
     - 弹出cur_idx，记录当前高度cur_h
     - 左边界：栈空则-1，否则st[-1]
     - 宽度 = l - left - 1，计算面积，更新最大值
   - l入栈
3. 返回max_size

```
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        st=[]
        max_size=0
        heights.append(0)
        for l,h in enumerate(heights):
            while st and h<heights[st[-1]]:
                cur_idx=st.pop()
                cur_h=heights[cur_idx]
                left=st[-1] if st else -1
                width=l-left-1
                cur_size=width*cur_h
                if cur_size>max_size:
                    max_size=cur_size
            st.append(l)
        return max_size
```


---

## 215. 数组中的第K个最大元素

### 核心思路

维护一个容量为k的**小根堆**。遍历数组，不断入堆；堆超过k个元素就弹出最小的。遍历结束，堆顶就是第k大。

1. 初始化空堆
2. 遍历每一个数字x：
   - heappush 压入堆
   - 如果堆长度>k，弹出堆顶最小值
3. 最后返回堆顶 heap[0]


```
import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            heapq.heappush(heap, x)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
```


---

## 347. 前 K 个高频元素

### 核心思路

先用Counter统计每个数字出现频次；再用容量k的小根堆，堆里面存 `(频次,数字)`，频次作为比较依据，过滤出频次最高k个。


1. Counter统计nums频次
2. 初始化空堆，遍历（num, freq）键值对
   - push (freq, num)
   - 堆长度>k就弹出频次最小的
3. 遍历堆，收集里面的数字返回


```
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        head=[]
        for num,freq in count.items():
            heapq.heappush(head,(freq,num))
            if len(head)>k:
                heapq.heappop(head)
        res=[]
        for item in head:
            num=item[1]
            res.append(num)
        return res
```


---

## 295. 数据流的中位数（双堆模板）

### 核心思路

**一个大根堆(left)存较小一半数字，一个小根堆(right)存较大一半数字**

1. **init**：left、right两个空堆
2. addNum：
   - 优先压入左堆（负数）
   - 如果左堆最大值 > 右堆最小值：把左边最大挪到右边
   - 平衡数量：left最多比right多1；right不能超过left
3. findMedian：
   - 总数奇数：中位数 = -left[0]
   - 总数偶数：中位数 = (-left[0] + right[0]) / 2


```
import heapq
class MedianFinder:
    def __init__(self):
        self.left=[]
        self.right=[]
    def addNum(self, num: int) -> None:
        heapq.heappush(self.left,-num)
        if self.left and self.right and (-self.left[0])>self.right[0]:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        if len(self.right) > len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)
    def findMedian(self) -> float:
        total = len(self.left) + len(self.right)
        if total % 2 == 1:

            return -self.left[0]
        else:

            return (-self.left[0] + self.right[0]) / 2
```

---

## 121. 买卖股票的最佳时机

### 核心思路
只能买卖一次。遍历的时候**记录到当前为止的历史最低价格**，每天都尝试用今天价格减去最低价，更新最大利润。

1. min_price初始无穷大，max_profit=0
2. 遍历价格p：
   - p比min_price更小 → 更新min_price
   - 否则：计算利润，更新max_profit
3. 返回max_profit


```
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                max_profit = max(max_profit, p - min_price)
        return max_profit
```

---

## 55. 跳跃游戏

### 核心思路

cover：当前能跳到的最远下标。逐个遍历i（i不能超过cover），不断更新cover；如果cover >= n-1直接True。遍历结束达不到返回False。

1. i=0, cover=0, n=数组长度
2. while i <= cover：
   - cover = max(i + nums[i], cover)
   - cover已经到最后下标 → return True
   - i += 1
3. return False


```
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums)==1:
            return True
        i=0
        cover=0
        n=len(nums)
        while i<=cover:
            cover=max(i+nums[i],cover)
            if cover>=n-1:
                return True
            i+=1
        return False
```

---

## 45. 跳跃游戏 II
### 核心思路
cur：当前这一跳能到达的边界；cur_next：下一跳能到达的最远边界。走到cur的时候，必须跳一次，更新cur=cur_next，计数+1。

1. n=len(nums)，长度为1直接返回0
2. cur=0, cur_next=0, res=0
3. 遍历i从0~n-1：
   - cur_next = max(i+nums[i], cur_next)
   - 如果i == cur：
     - 不是终点：跳一次 res += 1，cur = cur_next
     - cur已经到终点直接break
4. 返回res

```
class Solution:
    def jump(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        cur=0
        cur_next=0
        result=0
        for i in range(n):
            cur_next=max(i+nums[i],cur_next)
            if i==cur:
                if cur<n-1:
                    result+=1
                    cur=cur_next
                if cur>=n-1:
                    break
        return result
```

---

## 763. 划分字母区间
### 核心思路
先预处理：记录每个字母**最后一次出现的下标**。遍历字符串，不断更新当前片段的右边界right；当i走到right，说明这个区间可以切一刀。

1. 遍历一遍s，记录每个char最后出现位置last字典
2. left=0，right=0，res存答案
3. 枚举i,字符j：
   - right = max(right, last[j])
   - i == right：分割，长度 i-left+1 加入结果，left=i+1
4. 返回res


```
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last={}
        for idx ,char in enumerate(s):
            last[char]=idx
        res=[]
        left=0
        right=0
        for i ,j in enumerate(s):
            right=max(right,last[j])
            if i==right:
                res.append(i-left+1)
                left=i+1
        return res
```

