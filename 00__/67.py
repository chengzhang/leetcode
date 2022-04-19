
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        if m < n:
            a, b, m, n = b, a, n, m
        res, x = [], 0
        for idx in range(m):
            i = int(a[idx])
            j = int(b[idx]) if idx < n else 0
            x, r = divmod(i+j+x, 2)
            res.append(r)
        if x:
            res.append(x)
        return ''.join([str(i) for i in reversed(res)])
