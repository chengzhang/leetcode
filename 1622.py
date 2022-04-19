
class Fancy:

    def __init__(self):
        self.nums = []
        self.w = [1]
        self.b = [0]

    def append(self, val: int) -> None:
        self.nums.append(val)
        self.w.append(self.w[-1])
        self.b.append(self.b[-1])

    def addAll(self, inc: int) -> None:
        self.b[-1] += inc

    def multAll(self, m: int) -> None:
        self.w[-1] *= m
        self.b[-1] *= m

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.nums):
            return -1
        f = self.w[-1] // self.w[idx]
        res = f * self.nums[idx] + self.b[-1] - f * self.b[idx]
        res = res % 100000007
        return res


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)