from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        parts = []
        for n in nums:
            if not parts or n != parts[-1][-1] + 1:
                parts.append([n])
            else:
                parts[-1].append(n)
        res = []
        for p in parts:
            if len(p) == 1:
                res.append(str(p[0]))
            else:
                res.append('{}->{}'.format(p[0], p[-1]))
        return res


if __name__ == '__main__':
    cases = [
        ([0,1,2,4,5,7], ["0->2","4->5","7"]),
        ([0,2,3,4,6,8,9], ["0","2->4","6","8->9"]),
        ([], []),
        ([-1], ["-1"]),
        ([0], ["0"]),
    ]
    sln = Solution()
    for nums, golden in cases:
        res = sln.summaryRanges(nums)
        print(golden, res)
        assert golden == res
