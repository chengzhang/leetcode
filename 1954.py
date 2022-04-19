class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        n = 0
        x = 0
        while x < neededApples:
            n += 1
            z = 3 * n * (n + 1) // 2
            y = 8 * z - 4 * n - 4 * 2 * n
            x += y
        return 8*n


if __name__ == '__main__':
    cases = [
        (0, 0),
        (1, 8),
        (2, 8),
        (3, 8),
        (12, 8),
        (13, 16),
        (14, 16),
        (1000000000, 5040),
    ]
    sln = Solution()
    for num, golden in cases:
        res = sln.minimumPerimeter(num)
        assert golden == res
