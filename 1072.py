from typing import List
from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = Counter()
        for row in matrix:
            p0 = tuple(i for i, x in enumerate(row) if not x)
            p1 = tuple(i for i, x in enumerate(row) if x)
            if p0 > p1:
                p0, p1 = p1, p0
            cnt[p0] += 1
            cnt[p1] += 1
        return cnt.most_common(1)[0][1]


if __name__ == '__main__':
    cases = [
        ([[0,1],[1,1]], 1),
        ([[0,1],[1,0]], 2),
        ([[0,0,0],[0,0,1],[1,1,0]], 2),
    ]
    sln = Solution()
    for matrix, golden in cases:
        res = sln.maxEqualRowsAfterFlips(matrix)
        print(golden, res)
        assert golden == res
