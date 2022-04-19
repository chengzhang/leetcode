from typing import List
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m == 1 or n == 1:
            return 0
        res = 0
        wall = [[2 * 10**4 for _ in range(n)] for _ in range(m)]
        # TODO: assign one num to a iterable
        visited = [[False for _ in range(n)] for _ in range(m)]
        min_heap = []
        i, j = 0, 0
        for s, dr, dc in [(n-1, 0, 1), (m-1, 1, 0), (n-1, 0, -1), (m-1, -1, 0)]:
            for _ in range(s):
                wall[i][j] = heightMap[i][j]
                heapq.heappush(min_heap, (wall[i][j], i, j))
                i += dr
                j += dc
        while min_heap:
            w, i, j = heapq.heappop(min_heap)
            if visited[i][j]:
                continue
            visited[i][j] = True
            res += max(0, w - heightMap[i][j])
            for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    # TODO: mutable heap in python
                    wall[x][y] = min(wall[x][y], max(w, heightMap[i][j]))
                    heapq.heappush(min_heap, (wall[x][y], x, y))
        return res


    def trapRainWater_0(self, heightMap: List[List[int]]) -> int:
        res = 0
        m, n = len(heightMap), len(heightMap[0])
        wall = [[None for _ in range(n)] for _ in range(m)]
        i, j = 0, 0
        for s, dr, dc in [(n-1, 0, 1), (m-1, 1, 0), (n-1, 0, -1), (m-1, -1, 0)]:
            for _ in range(s):
                print(f'({i},{j})'),
                wall[i][j] = heightMap[i][j]
                i += dr
                j += dc
        for c in range(1, (min(m, n)+1)//2):
            mm, nn = m - c * 2, n - c * 2
            min_heap = []
            i, j = c, c
            if mm == 1:
                for d in range(nn):
                    j = c + d
                    print(f'({i},{j})'),
                    wall[i][j] = min(filter(lambda x: x, [
                        wall[i - 1][j], wall[i + 1][j],
                        wall[i][j - 1], wall[i][j + 1]
                    ]))
                    heapq.heappush(min_heap, (wall[i][j], i, j))
            elif nn == 1:
                for d in range(mm):
                    i = c + d
                    print(f'({i},{j})'),
                    wall[i][j] = min(filter(lambda x: x, [
                        wall[i - 1][j], wall[i + 1][j],
                        wall[i][j - 1], wall[i][j + 1]
                    ]))
                    heapq.heappush(min_heap, (wall[i][j], i, j))

            else:
                for s, dr, dc in [(nn-1, 0, 1), (mm-1, 1, 0), (nn-1, 0, -1), (mm-1, -1, 0)]:
                    for _ in range(s):
                        print(f'({i},{j})'),
                        # TODO: build in func NotNone
                        wall[i][j] = min(filter(lambda x: x, [
                            wall[i-1][j], wall[i+1][j],
                            wall[i][j-1], wall[i][j+1]
                        ]))
                        heapq.heappush(min_heap, (wall[i][j], i, j))
                        i += dr
                        j += dc
            while min_heap:
                w, i, j = heapq.heappop(min_heap)
                res += max(0, wall[i][j] - heightMap[i][j])
                wall[i][j] = max(wall[i][j], heightMap[i][j])
        return res


if __name__ == '__main__':
    cases = [
        ([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]], 4),
        ([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]], 10),
    ]
    sln = Solution()
    for hm, golden in cases:
        res = sln.trapRainWater(hm)
        print(golden, res)
        assert golden == res
