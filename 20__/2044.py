from typing import List
import functools
import operator


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_res = functools.reduce(operator.or_, nums, 0)
        N = len(nums)

        def dfs(subset, depth, max_cnt):
            if depth == N:
                or_res = functools.reduce(operator.or_, subset, 0)
                return max_cnt + 1 if or_res == max_or_res else max_cnt
            mc = dfs(subset, depth+1, max_cnt)
            subset.append(nums[depth])
            mc = dfs(subset, depth+1, mc)
            subset.pop()
            return mc

        return dfs([], 0, 0)


if __name__ == '__main__':
    cases = [
        ([3, 1], 2),
        ([2, 2, 2], 7),
        ([3, 2, 1, 5], 6),
    ]
    sln = Solution()
    for nums, golden in cases:
        res = sln.countMaxOrSubsets(nums)
        assert res == golden

