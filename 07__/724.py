from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        l_sum = [0]*(n+1)
        for i in range(n):
            l_sum[i+1] = l_sum[i] + nums[i]
        for i in range(n):
            if l_sum[i] == total - l_sum[i+1]:
                return i
        else:
            return -1
