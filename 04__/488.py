import re
import itertools
from collections import deque
from functools import lru_cache


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        board = self.collapse(board)
        hand = ''.join(sorted(hand))
        res = self.dfs(board, hand)
        return res if res < 6 else -1

    @staticmethod
    def collapse(lst):
        char_cnt = []
        for i, c in enumerate(lst):
            if not char_cnt:
                char_cnt.append([c, 1])
            elif char_cnt[-1][0] == c:
                char_cnt[-1][1] += 1
            elif char_cnt[-1][1] > 2:
                char_cnt.pop()
                if char_cnt and char_cnt[-1][0] == c:
                    char_cnt[-1][1] += 1
                else:
                    char_cnt.append([c, 1])
            else:
                char_cnt.append([c, 1])
        if char_cnt and char_cnt[-1][1] > 2:
            char_cnt.pop()
        ret = []
        for char, cnt in char_cnt:
            ret.extend([char] * cnt)
        ret = ''.join(ret)
        return ret

    @lru_cache(None)
    def dfs(self, board, hand):
        if not board:
            return 0
        bl, hl = len(board), len(hand)
        ret = 6
        for i, j in itertools.product(range(len(board)+1), range(len(hand))):
            if j > 0 and hand[j-1] == hand[j]:
                continue
            if i > 0 and board[i-1] == hand[j]:
                continue
            new_board = self.collapse(board[:i] + hand[j] + board[i:])
            new_hand = hand[:j] + hand[j+1:]
            sub_res = self.dfs(new_board, new_hand)
            ret = min(ret, sub_res+1)
        return ret


if __name__ == '__main__':
    cases = [
        ("WRRBBW", "RB", -1),
        ("WWRRBBWW", "WRBRW", 2),
        ("G", "GGGGG", 2),
        ("RBYYBBRRB", "YRBGB", 3),
    ]
    sln = Solution()
    for board, hand, golden in cases:
        res = sln.findMinStep(board, hand)
        print(golden, res)
        assert golden == res
