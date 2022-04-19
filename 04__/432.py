from collections import defaultdict
from typing import Set

class AllOne:
    def __init__(self):
        self.LB, self.UB = 0, 10**8
        self.next_cnt = {self.LB: self.UB}
        self.prev_cnt = {self.UB: self.LB}
        self.key_cnt = defaultdict(int)
        self.cnt_key = defaultdict(Set)

    def inc(self, key: str) -> None:
        cnt = self.key_cnt[key]
        self.key_cnt[key] = cnt + 1
        self.cnt_key[cnt+1].add(key)
        if cnt:
            self.cnt_key[cnt].remove(key)

        prv = self.prev_cnt[cnt]
        nxt = self.next_cnt[cnt]

        self.next_cnt[cnt] = cnt+1
        self.prev_cnt[cnt+1] = cnt
        if len(self.cnt_key[cnt+1]) == 1:
            self.next_cnt[cnt+1] = nxt
            self.prev_cnt[nxt] = cnt+1
        if not self.cnt_key[cnt]:
            self.next_cnt[prv] = cnt+1
            self.prev_cnt[cnt+1] = prv

    def dec(self, key: str) -> None:
        cnt = self.key_cnt[key]
        self.cnt_key[cnt].remove(key)
        self.cnt_key[cnt+1].add(key)
        


    def getMaxKey(self) -> str:


    def getMinKey(self) -> str:



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()