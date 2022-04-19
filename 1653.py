class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        b_cnt, a_cnt = [0]*(n+1), [0]*(n+1)
        for i in range(n):
            b_cnt[i+1] = b_cnt[i] + int(s[i] == 'b')
        for i in reversed(range(n)):
            a_cnt[i] = a_cnt[i+1] + int(s[i] == 'a')
        return min(a + b for a, b in zip(a_cnt, b_cnt))


if __name__ == '__main__':
    cases = [
        ("aababbab", 2),
        ("bbaaaaabb", 2),
    ]
    sln = Solution()
    for s, golden in cases:
        res = sln.minimumDeletions(s)
        print(golden, res)
        assert golden == res
