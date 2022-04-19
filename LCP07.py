from typing import List
from collections import defaultdict


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        adj = defaultdict(set)
        for f, t in relation:
            adj[f].add(t)
        layer, nxt_layer = [0], []
        for i in range(k):
            nxt_layer.clear()
            for node in layer:
                nxt_layer.extend(adj[node])
            layer, nxt_layer = nxt_layer, layer
        return layer.count(n-1)


if __name__ == '__main__':
    cases = [
        (5, [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], 3, 3),
        (3, [[0,2],[2,1]], 2, 0),
    ]
    sln = Solution()
    for n, rel, k, golden in cases:
        res = sln.numWays(n, rel, k)
        print(golden, res)
        assert golden == res
