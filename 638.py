from functools import lru_cache
from typing import List


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def __raw_price(x):
            return sum(p * n for p, n in zip(price, x))
        new_special = [x for x in special if __raw_price(x[:-1]) > x[-1]]

        @lru_cache(None)
        def __dfs(cur_needs):
            min_price = __raw_price(cur_needs)
            for sp in new_special:
                if all(i <= j for i, j in zip(sp[:-1], cur_needs)):
                    nxt_needs = tuple(i - j for i, j in zip(cur_needs, sp[:-1]))
                    min_price = min(min_price, sp[-1] + __dfs(nxt_needs))
            return min_price

        return __dfs(tuple(needs))


if __name__ == '__main__':
    cases = [
        ([2,5], [[3,0,5],[1,2,10]], [3,2], 14),
        ([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1], 11),
    ]
    sln = Solution()
    for price, special, needs, golden in cases:
        res = sln.shoppingOffers(price, special, needs)
        print(golden, res)
        assert golden == res
