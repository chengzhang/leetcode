from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        l = len(arr)
        for i, n in enumerate(arr):
            step, times = 1, 1
            while times:
                lo = max(0, i - step + 1)
                hi = min(l - 1, i + step - 1)
                times = max(0, hi - lo + 1 - step + 1)
                step += 2
                res += n * times
        return res


if __name__ == '__main__':
    cases = [
        ([1,4,2,5,3], 58),
        ([1,2], 3),
        ([10,11,12], 66),
    ]
    sln = Solution()
    for arr, golden in cases:
        res = sln.sumOddLengthSubarrays(arr)
        print(golden, res)
        assert golden == res
