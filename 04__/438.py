from typing import List
from collections import Counter

class Solution:
    def findAnagrams0(self, s: str, p: str) -> List[int]:
        def idx(c):
            return ord(c) - ord('a')
        m, n = len(s), len(p)
        s_cnt, p_cnt = [0]*26, [0]*26
        for i in s[:n-1]:
            s_cnt[idx(i)] += 1
        for i in p:
            p_cnt[idx(i)] += 1
        res = []
        for i in range(0, m-n+1):
            s_cnt[idx(s[i+n-1])] += 1
            if s_cnt == p_cnt:
                res.append(i)
            s_cnt[idx(s[i])] -= 1
        return res

    def findAnagrams1(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        s_cnt, p_cnt = Counter(s[:n-1]), Counter(p)
        res = []
        for i in range(0, m-n+1):
            s_cnt[s[i+n-1]] += 1
            if s_cnt == p_cnt:
                res.append(i)
            s_cnt[s[i]] -= 1
            if not s_cnt[s[i]]:
                s_cnt.pop(s[i])
        return res
