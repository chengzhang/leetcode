from typing import List
from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dep = defaultdict(list)
        for i, h in enumerate(manager):
            dep[h].append(i)
        final = {dep[-1][0]: informTime[dep[-1][0]]}
        res = 0
        while final:
            h, t = final.popitem()
            res = max(res, t)
            final.update((final[x], t + informTime[x]) for x in dep[h])
        return res


if __name__ == '__main__':
    cases = [
        (1, 0, [-1], [0]),
        (),
        (),
    ]