class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return '0'
        res = ''
        base = 0
        while n:
            mod = n % (2**(base+1))
            bit = int(mod > 0)
            n -= bit * ((-2) ** base)
            res = str(bit) + res
            base += 1
        return res


if __name__ == '__main__':
    cases = [
        (3, '111'),
        (2, '110'),
        (4, '100'),
    ]
    sln = Solution()
    for n, golden in cases:
        res = sln.baseNeg2(n)
        print(golden, res)
        assert golden == res
