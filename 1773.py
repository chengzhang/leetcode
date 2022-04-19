from typing import List
from collections import defaultdict


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index = {k: defaultdict(int) for k in ['type', 'color', 'name']}
        for i, (ty, co, na) in enumerate(items):
            index['type'][ty] += 1
            index['color'][co] += 1
            index['name'][na] += 1
        return index[ruleKey][ruleValue]


if __name__ == '__main__':
    cases = [
        ([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver", 1),
        ([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone", 2),
    ]
    sln = Solution()
    for items, key, value, golden in cases:
        res = sln.countMatches(items, key, value)
        print(golden, res)
        assert golden == res
