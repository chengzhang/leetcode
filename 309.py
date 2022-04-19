from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        prv, nxt = [-prices[0], 0, 0], [0, 0, 0]
        for i in range(1, len(prices)):
            nxt[0] = max(prv[0], prv[2] - prices[i])
            nxt[1] = prv[0] + prices[i]
            nxt[2] = max(prv[1], prv[2])
            prv, nxt = nxt, prv
        return max(prv)


if __name__ == '__main__':
    cases = [
        ([1, 2, 3, 0, 2], 3)
    ]
    sln = Solution()
    for prices, golden in cases:
        res = sln.maxProfit(prices)
        print(golden, res)
        assert golden == res
