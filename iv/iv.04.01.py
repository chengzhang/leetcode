from typing import List
from collections import defaultdict
from collections import deque


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        visited = [False for _ in range(n)]
        adj = defaultdict(set)
        for f, t in graph:
            adj[f].add(t)
        candidates = deque([start])
        visited[start] = True
        while candidates:
            node = candidates.popleft()
            if node == target:
                return True
            for nxt in adj[node]:
                if not visited[nxt]:
                    candidates.append(nxt)
                    visited[nxt] = True
        return False


if __name__ == '__main__':
    cases = [
        (3, [[0, 1], [0, 2], [1, 2], [1, 2]], 0, 2, True),
        (5, [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], 0, 4, True),
    ]
    sln = Solution()
    for i, (n, graph, start, target, golden) in enumerate(cases):
        res = sln.findWhetherExistsPath(n, graph, start, target)
        print(f'case {i}, {golden}, {res}')
        assert golden == res
