from typing import List
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        count = 0 
        while q:
            cur = q.popleft()
            count += 1
            for nxt in graph[cur]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    q.append(nxt)
        return count == numCourses
if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1, 0]]))  # Output: True
    print(sol.canFinish(2, [[1, 0], [0, 1]]))  # Output: False