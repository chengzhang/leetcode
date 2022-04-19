import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.out = nums.copy()
        self._init_shuffle()

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        i, j = random.randint(0, len(self.out)-1), random.randint(0, len(self.out)-1)
        self.out[i], self.out[j] = self.out[j], self.out[i]
        return self.out

    def _init_shuffle(self):
        for i in range(len(self.out)):
            j = random.randint(0, len(self.out)-1)
            self.out[i], self.out[j] = self.out[j], self.out[i]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()