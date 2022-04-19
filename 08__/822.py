from typing import List


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        repeat = set()
        rest = []
        for f, b in zip(fronts, backs):
            if f == b:
                repeat.add(f)
            if f not in repeat:
                rest.append(f)
            if b not in repeat:
                rest.append(b)
        rest.sort()
        if not rest:
            return 0
        return rest[0]


if __name__ == '__main__':
    cases = [
        ([1,2,4,4,7], [1,3,4,1,3], 2),
    ]
    sln = Solution()
    for fronts, backs, golden in cases:
        res = sln.flipgame(fronts, backs)
        print(golden, res)
        assert golden == res
