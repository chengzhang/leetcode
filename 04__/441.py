# coding = utf8

"""
二分查找
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mi = (lo + hi) // 2
            total = mi * (mi + 1) // 2
            next_total = (mi+1)*(mi+2) // 2
            if total == n:
                return mi
            elif total < n:
                if next_total <= n:
                    lo = mi + 1
                else:
                    return mi
            else:
                hi = mi
        return lo


if __name__ == '__main__':
    cases = [
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 2),
        (6, 3),
        (7, 3),
        (8, 3),
    ]
    sln = Solution()
    for case in cases:
        n, golden = case
        res = sln.arrangeCoins(n)
        print(golden, res)
        assert golden == res
