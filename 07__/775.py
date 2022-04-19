from typing import List


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        return all(i == x or abs(i-x) == 1 for i, x in enumerate(nums))


if __name__ == '__main__':
    cases = [
        ([0, 1, 2], True),
        ([0, 2, 1], True),
        ([1, 0, 2], True),
        ([1, 2, 0], False),
        ([2, 0, 1], False),
        ([2, 1, 0], False),
    ]
    sln = Solution()
    for nums, golden in cases:
        res = sln.isIdealPermutation(nums)
        print(golden, res)
        assert golden == res
