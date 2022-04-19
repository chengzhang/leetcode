from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i-1, 0, -1):
                res[j] = res[j-1] + res[j]
        return res


if __name__ == '__main__':
    cases = [
        (0, [1]),
        (1, [1, 1]),
        (2, [1, 2, 1]),
        (3, [1, 3, 3, 1]),
        (4, [1, 4, 6, 4, 1]),
    ]
    sln = Solution()
    for rowIndex, golden in cases:
        res = sln.getRow(rowIndex)
        print(golden, res)
        assert golden == res
