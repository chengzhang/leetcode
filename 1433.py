from collections import Counter


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def accumulate(s):
            cnt = Counter(s)
            acc = [0] * 27
            for i in range(26):
                ch = chr(i + ord('a'))
                acc[i+1] += acc[i] + cnt[ch]
            return acc
        acc1, acc2 = accumulate(s1), accumulate(s2)
        diff = [i - j for i, j in zip(acc1, acc2)]
        return max(diff) <= 0 or min(diff) >= 0

    def checkIfCanBreak_1(self, s1: str, s2: str) -> bool:
        s1 = sorted(list(s1))
        s2 = sorted(list(s2))
        if s1 > s2:
            s1, s2 = s2, s1
        for c1, c2 in zip(s1, s2):
            if c1 > c2:
                return False
        return True

