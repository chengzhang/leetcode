from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        n = len(inventory)
        res = 0
        for i, v in enumerate(inventory):
            d = v - inventory[i+1] if i + 1 < n else v
            w = i + 1
            h, orders = divmod(orders, w)
            if not h:
                res += orders * v
                break
            if d <= h:
                res += w * (v+v-d+1) * d // 2
                orders += (h-d) * w
            else:
                res += w * (v+v-h+1) * h // 2
                res += orders * (v-h+1)
                break
        return res



