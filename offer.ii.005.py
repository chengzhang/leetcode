# coding = utf8
from typing import List
from collections import defaultdict

"""
"""


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        char_2_indexes = defaultdict(set)
        for i, word in enumerate(words):
            for c in word:
                char_2_indexes[c].add(i)
        nbs = defaultdict(set)
        for c, indexes in char_2_indexes.items():
            lst = list(indexes)
            for i, x in enumerate(lst):
                for y in lst[i+1:]:
                    nbs[x].add(y)
                    nbs[y].add(x)
        len_cnt = defaultdict(int)
        for w in words:
            len_cnt[len(w)] += 1
        ordered_len_cnt = sorted(len_cnt.items(), key=lambda x: x[0], reverse=True)
        res = 0
        for i, w in enumerate(words):
            nb_len_cnt = defaultdict(int)
            nb_len_cnt[len(w)] += 1
            for nb in nbs[i]:
                nb_len_cnt[len(words[nb])] += 1
            for length, cnt in ordered_len_cnt:
                nb_cnt = nb_len_cnt.get(length, 0)
                if cnt > nb_cnt:
                    res = max(len(w)*length, res)
        return res


if __name__ == '__main__':
    cases = [
        (["abcw","baz","foo","bar","fxyz","abcdef"], 16),
        (["a","ab","abc","d","cd","bcd","abcd"], 4),
        (["a","aa","aaa","aaaa"], 0),
    ]
    sln = Solution()
    for words, golden in cases:
        res = sln.maxProduct(words)
        print(golden, res)
        assert golden == res
