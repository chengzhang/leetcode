from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in asteroids:
            if a < 0:
                while res and 0 < res[-1] < -a:
                    res.pop()
                if not res or res[-1] < 0:
                    res.append(a)
                elif res[-1] == -a:
                    res.pop()
                else:
                    pass
            else:
                res.append(a)
        return res
