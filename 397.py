from collections import deque


class Solution:
    def integerReplacement(self, n: int) -> int:
        q = deque([(n, 0)])
        visited = {n: 0}
        while q:
            num, step = q.popleft()
            if num == 1:
                return step
            if num % 2 == 0:
                if num//2 not in visited:
                    q.append((num//2, step+1))
            else:
                if num+1 not in visited:
                    q.append((num+1, step+1))
                if num - 1 not in visited:
                    q.append((num-1, step+1))


if __name__ == '__main__':
    cases = [
        (1, 0),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 3),
        (6, 3),
        (7, 4),
        (8, 3),
    ]
    sln = Solution()
    for n, golden in cases:
        res = sln.integerReplacement(n)
        print(golden, res)
        assert golden == res
