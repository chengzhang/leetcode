from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        for i, t in enumerate(timeSeries):
            res += duration
            if i > 0 and timeSeries[i-1] + duration < t:
                res -= duration - (t - timeSeries[i-1])
        return res


if __name__ == '__main__':
    cases = [
        (),
    ]