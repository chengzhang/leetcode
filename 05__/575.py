from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))


if __name__ == '__main__':
    cases = [
        ([1,1,2,2,3,3], 3),
        ([1,1,2,3], 2),
    ]
    sln = Solution()
    for candies, golden in cases:
        res = sln.distributeCandies(candies)
        print(golden, res)
        assert golden == res
