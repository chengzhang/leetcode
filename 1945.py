class Solution:
    def getLucky(self, s: str, k: int) -> int:
        arr = [ord(c) - ord('a') + 1 for c in s]
        s = ''.join(str(i) for i in arr)
        res = 0
        for _ in range(k):
            res = sum(int(i) for i in s)
            s = str(res)
        return res
