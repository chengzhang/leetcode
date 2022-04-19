from collections import defaultdict, Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def split_digits(a):
            digits = []
            while a:
                a, mod = divmod(a, 10)
                digits.append(mod)
            return len(digits), Counter(digits)
        dn, cdn = split_digits(n)
        x = 1
        while True:
            dx, cdx = split_digits(x)
            if dx > dn:
                break
            if dx == dn and cdn == cdx:
                return True
            x *= 2
        return False


if __name__ == '__main__':
    cases = [
        (1, True),
        (2, True),
        (3, False),
        (4, True),
        (5, False),
        (10, False),
        (16, True),
        (24, False),
        (46, True),
    ]
    sln = Solution()
    for n, golden in cases:
        res = sln.reorderedPowerOf2(n)
        print(golden, res)
        assert golden == res
