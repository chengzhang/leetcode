from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        top = [0, 0, 0]
        cnt = [0, 0, 0]
        for n in nums:
            try:
                idx = top.index(n)
            except ValueError:
                idx = cnt.index(0)
            top[idx] = n
            cnt[idx] += 1
            if min(cnt) == 1:
                for i in range(len(cnt)):
                    cnt[i] -= 1
        res = []
        for n, c in zip(top, cnt):
            if c and nums.count(n) > len(nums) // 3:
                res.append(n)
        return res


if __name__ == '__main__':
    cases = [
        ([3,2,3], [3]),
        ([1], [1]),
        ([1,1,1,2,2,2,3,3], [1,2]),
    ]
    sln = Solution()
    for nums, golden in cases:
        res = sln.majorityElement(nums)
        assert set(res) == set(golden)
