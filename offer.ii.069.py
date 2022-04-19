from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        N = len(arr)
        lo, hi = 1, N-2
        ans = lo
        while lo <= hi:
            mi = (lo + hi) // 2
            if arr[mi] > arr[mi-1]:
                ans = mi
                lo = mi + 1
            else:
                hi = mi - 1
        return ans


if __name__ == '__main__':
    cases = [
        ([0, 1, 0], 1),
        ([1, 3, 5, 4, 2], 2),
        ([0, 10, 5, 2], 1),
        ([3, 4, 5, 1], 2),
    ]
    sln = Solution()
    for arr, golden in cases:
        res = sln.peakIndexInMountainArray(arr)
        print(golden, res)
        assert golden == res
