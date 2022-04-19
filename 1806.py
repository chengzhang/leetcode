class Solution:
    def reinitializePermutation(self, n: int) -> int:
        nxt = {}
        for i in range(n):
            if i & 1:
                nxt[i] = n // 2 + (i - 1) // 2
            else:
                nxt[i] = i // 2
        lens = set()
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            step = 1
            node = i
            while nxt[node] != i:
                node = nxt[node]
                step += 1
                visited[node] = True
            lens.add(step)

        def __lcm(x, y):
            a, b = x, y
            while a % b != 0:
                a, b = b, a % b
            return x * y // b

        lcm = lens.pop()  # 最小公倍数缩写
        while lens:
            step = lens.pop()
            lcm = __lcm(lcm, step)
        return lcm


if __name__ == '__main__':
    cases = [
        (2, 1),
        (4, 2),
        (6, 4)
    ]
    sln = Solution()
    for n, golden in cases:
        res = sln.reinitializePermutation(n)
        print(golden, res)
        assert golden == res
