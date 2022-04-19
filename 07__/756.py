
from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def char2int(char):
            return ord(char) - ord('A')
        bottom = [char2int(c) for c in bottom]
        allowed_mat = [[set() for _ in range(7)] for _ in range(7)]
        for i, j, k in allowed:
            i, j, k = char2int(i), char2int(j), char2int(k)
            allowed_mat[i][j].add((k, i, j))
        n = len(bottom)
        candidates = [{(bottom[0], 42, 42)}]
        for i in range(1, n):
            nxt_candidates = [{(bottom[i], 42, 42)}]
            for j in range(i):
                tops = set()
                for a, al, ar in candidates[j]:
                    for b, bl, br in nxt_candidates[j]:
                        if ar == bl:
                            tops |= allowed_mat[a][b]
                nxt_candidates.append(tops)
                if not tops:
                    return False
            candidates = nxt_candidates
        return True


if __name__ == '__main__':
    cases = [
        ("BCD", ["BCG", "CDE", "GEA", "FFF"], True),
        ("AABA", ["AAA", "AAB", "ABA", "ABB", "BAC"], False),
        ("AAAA", ["AAB","AAC","BCD","BBE","DEF"], False),
    ]
    sln = Solution()
    for bottom, allowed, golden in cases:
        res = sln.pyramidTransition(bottom, allowed)
        print(golden, res)
        assert golden == res
