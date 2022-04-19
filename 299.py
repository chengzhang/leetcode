class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        digits_s, digits_g = [0] * 10, [0] * 10
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                s, g = int(s), int(g)
                digits_s[s] += 1
                digits_g[g] += 1
        for s, g in zip(digits_s, digits_g):
            cows += min(s, g)
        return f'{bulls}A{cows}B'


if __name__ == '__main__':
    cases = [
        ("1807", "7810", '1A3B'),
        ("1123", "0111", '1A1B'),
        ("1", "0", "0A0B"),
        ("1", "1", "1A0B"),
    ]
    sln = Solution()
    for s, g, golden in cases:
        res = sln.getHint(s, g)
        print(golden, res)
        assert golden == res
