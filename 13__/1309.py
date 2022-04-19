# coding = utf8


class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        N = len(s)
        i = 0
        while i < N:
            if s[i] in '12':
                if i + 2 < N and s[i+2] == '#':
                    res.append(self.decode_one(s[i:i+2]))
                    i += 2
                else:
                    res.append(self.decode_one(s[i]))
            else:
                res.append(self.decode_one(s[i]))
            i += 1
        return ''.join(res)

    def decode_one(self, s: str) -> str:
        if len(s) == 1:
            return chr(ord('a') + int(s) - 1)
        else:
            return chr(ord('j') + int(s) - 10)


if __name__ == '__main__':
    cases = [
        ("10#11#12", "jkab"),
        ("1326#", "acz"),
        ("25#", "y"),
        ("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#", "abcdefghijklmnopqrstuvwxyz"),
    ]
    sln = Solution()
    for case in cases:
        s, golden = case
        res = sln.freqAlphabets(s)
        print(golden, res)
        assert golden == res
