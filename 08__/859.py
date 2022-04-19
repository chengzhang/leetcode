from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        diff = [(c1, c2) for c1, c2 in zip(s, goal) if c1 != c2]
        if len(diff) == 1 or len(diff) > 2:
            return False
        if len(diff) == 2:
            return diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]
        # len(diff) == 0
        cnt = Counter(s)
        return cnt.most_common(1)[0][1] > 1


if __name__ == '__main__':
    cases = [
        ('ab', 'ba', True),
        ('ab', 'ab', False),
        ('aa', 'aa', True),
        ('aaaaaaabc', 'aaaaaaacb', True),
    ]
    sln = Solution()
    for s, s1, golden in cases:
        res = sln.buddyStrings(s, s1)
        print(golden, res)
        assert golden == res
