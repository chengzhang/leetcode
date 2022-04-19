class Solution:
    def generateTheString(self, n: int) -> str:
        res = 'a' * (n-1)
        if n % 2 == 0:
            res += 'b'
        return res