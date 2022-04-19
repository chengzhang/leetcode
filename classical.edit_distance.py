def edit_distance(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
    return dp[m][n]


if __name__ == '__main__':
    cases = [
        ('', '', 0),
        ('', 'a', 1),
        ('a', '', 1),
        ('ab', 'a', 1),
        ('ab', 'ab', 0),
        ('ac', 'ab', 1),
        ('a', 'ab', 1),
        ('foo', 'bar', 3),
        ('hello', 'world', 4),
    ]
    for s1, s2, golden in cases:
        res = edit_distance(s1, s2)
        print(golden, res)
        assert golden == res


