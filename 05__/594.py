from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = 0
        for k, v in cnt.items():
            if k + 1 in cnt:
                res = max(res, v + cnt[k+1])
        return res

