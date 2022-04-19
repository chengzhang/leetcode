class Solution:
    def getMoneyAmount(self, n: int) -> int:
        v = [[0 for _ in range(n+2)] for _ in range(n+2)]
        for d in range(1, n):
            for i in range(1, n-d+1):
                j = i + d
                v[i][j] = min([x+max(v[i][x-1], v[x+1][j]) for x in range(i, j+1)])
        return v[1][n]


if __name__ == '__main__':
    cases = [
        (10, 16),
        (1, 0),
        (2, 1),
        (3, 2),
        (4, 4),
    ]
    sln = Solution()
    for n, golden in cases:
        res = sln.getMoneyAmount(n)
        print(golden, res)
        assert golden == res
