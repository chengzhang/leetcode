class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        lo, hi = 1, num
        while lo < hi:
            mi = (lo + hi) // 2
            pow2 = mi ** 2
            if pow2 == num:
                return True
            elif pow2 < num:
                lo = mi + 1
            else:
                hi = mi
        return False


if __name__ == '__main__':
    cases = [
        (1, True),
        (2, False),
        (3, False),
        (4, True),
        (5, False),
        (6, False),
        (7, False),
        (8, False),
        (9, True),
    ]
    sln = Solution()
    for num, golden in cases:
        res = sln.isPerfectSquare(num)
        print(golden, res)
        assert golden == res
