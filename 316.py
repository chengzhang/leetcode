from collections import Counter, defaultdict


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_cnt = Counter(s)
        visited = defaultdict(bool)
        stack = []
        for char in s:
            if not visited[char]:
                while stack and stack[-1] > char and char_cnt[stack[-1]]:
                    prv = stack.pop()
                    visited[prv] = False
                stack.append(char)
                visited[char] = True
            char_cnt[char] -= 1
        return ''.join(stack)


if __name__ == '__main__':
    cases = [
        ('bcabc', 'abc'),
        ('cbacdcbc', 'acdb'),
    ]
    sln = Solution()
    for s, golden in cases:
        res = sln.removeDuplicateLetters(s)
        print(golden, res)
        assert golden == res
