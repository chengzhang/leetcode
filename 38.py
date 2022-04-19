class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(1, n):
            num, cnt = self._count(res)
            res = self._say(num, cnt)
        return res

    def _count(self, s):
        num, cnt = [], []
        for c in s:
            if not num or c != num[-1]:
                num.append(c)
                cnt.append(1)
            else:
                cnt[-1] += 1
        return num, cnt

    def _say(self, num, cnt):
        res = []
        for n, c in zip(num, cnt):
            res.append(str(c))
            res.append(n)
        return ''.join(res)


if __name__ == '__main__':
    cases = [
        (1, '1'),
        (2, '11'),
        (3, '21'),
        (4, '1211'),
        (5, '111221'),
        (6, '312211'),
    ]
    sln = Solution()
    for n, golden in cases:
        res = sln.countAndSay(n)
        print(golden, res)
        assert golden == res
