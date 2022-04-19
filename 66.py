from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        x = 1
        for i in digits[::-1]:
            x, y = divmod(x + i, 10)
            res.append(y)
        if x:
            res.append(x)
        res.reverse()
        return res


if __name__ == '__main__':
    cases = [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([0], [1]),
        ([9], [1, 0]),
        ([1, 9], [2, 0]),
        ([9, 9], [1, 0, 0]),
    ]
    sln = Solution()
    for digits, golden in cases:
        res = sln.plusOne(digits)
        print(golden, res)
        assert golden == res
