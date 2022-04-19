from typing import List
from itertools import product
from collections import deque
import heapq


class Solution:
    def shortestPathBinaryMatrix_0(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        n = len(grid)
        visited = set()
        queue = deque([(1, 0, 0)])
        while queue:
            cost, i, j = queue.popleft()
            visited.add((i, j))
            if (i, j) == (n-1, n-1):
                return cost
            for di, dj in product([-1, 0, 1], repeat=2):
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < n and not grid[x][y] and (x, y) not in visited:
                    queue.append((cost+1, x, y))
        return -1

    def shortestPathBinaryMatrix_2(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        queue = [(1, 0, 0)]
        while queue:
            cost, i, j = heapq.heappop(queue)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if grid[i][j]:
                continue
            if (i, j) == (n-1, n-1):
                return cost
            for di, dj in product([-1, 0, 1], repeat=2):
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                    heapq.heappush(queue, (cost+1, x, y))
        return -1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def h(i, j):
            return min(n-i, n-j)
        n = len(grid)
        open_set, close_set = {(0, 0)}, set()
        pq = [(1+h(0, 0), 1, 0, 0)]
        while pq:
            gh, g, i, j = heapq.heappop(pq)
            if (i, j) in close_set:
                continue
            if grid[i][j]:
                continue
            if (i, j) == (n-1, n-1):
                return g
            close_set.add((i, j))
            open_set.remove((i, j))
            for di, dj in product([-1, 0, 1], repeat=2):
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < n and (x, y) not in close_set and (x, y) not in open_set:
                    heapq.heappush(pq, (g+1+h(x, y), g+1, x, y))
                    open_set.add((x, y))
        return -1


if __name__ == '__main__':
    cases = [
        ([[0,0,0],[1,1,0],[1,1,0]], 4),
        ([[0,1],[1,0]], 2),
        ([[1,0,0],[1,1,0],[1,1,0]], -1),
    ]
    sln = Solution()
    for grid, golden in cases:
        res = sln.shortestPathBinaryMatrix(grid)
        print(golden, res)
        assert golden == res
