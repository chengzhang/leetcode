from typing import List
import random


class Solution0:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.flips = self.new_flips()

    def flip(self) -> List[int]:
        idx = self.flips.pop()
        i, j = divmod(idx, self.n)
        return [i, j]

    def reset(self) -> None:
        self.flips = self.new_flips()

    def new_flips(self):
        return random.choices(range(self.m*self.n), k=min(self.m*self.n, 1000))


class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.rest = m * n
        self.empties = {}

    def flip(self) -> List[int]:
        self.rest -= 1
        x = random.randint(0, self.rest)
        i, j = self.empties.get(x, default=divmod(x, self.n))
        if self.rest in self.empties:
            self.empties[x] = self.empties[self.rest]
            self.empties.pop(self.rest)
        else:
            self.empties[x] = divmod(self.rest, self.n)
        return [i, j]

    def reset(self) -> None:
        self.empties.clear()
        self.rest = self.m * self.n


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()