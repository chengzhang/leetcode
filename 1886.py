from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        hit = [True] * 4
        for i, a0, b1, a2, b3 in zip(range(n), range(n), reversed(range(n)), reversed(range(n)), range(n)):
            for j, b0, a1, b2, a3 in zip(range(n), range(n), range(n), reversed(range(n)), reversed(range(n))):
                hit[0] &= mat[i][j] == target[a0][b0]
                hit[1] &= mat[i][j] == target[a1][b1]
                hit[2] &= mat[i][j] == target[a2][b2]
                hit[3] &= mat[i][j] == target[a3][b3]
        return any(hit)
