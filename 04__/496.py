from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        nearest_right = [-1] * 10001
        stack = []
        for i in range(n):
            while stack and nums2[stack[-1]] < nums2[i]:
                j = stack.pop()
                nearest_right[nums2[j]] = nums2[i]
            stack.append(i)
        res = [nearest_right[i] for i in nums1]
        return res


if __name__ == '__main__':
    cases = [
        ([4,1,2], [1,3,4,2], [-1,3,-1]),
        ([2,4], [1,2,3,4], [3,-1]),
    ]
    sln = Solution()
    for nums1, nums2, golden in cases:
        res = sln.nextGreaterElement(nums1, nums2)
        print(golden, res)
        assert golden == res
