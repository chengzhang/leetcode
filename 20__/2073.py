from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(i <= k and min(tickets[k], t) or min(tickets[k]-1, t) for i, t in enumerate(tickets))

