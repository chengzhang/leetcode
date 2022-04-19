import math


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        itr = minutesToTest // minutesToDie
        return math.ceil(math.log(buckets)/math.log(itr+1))
