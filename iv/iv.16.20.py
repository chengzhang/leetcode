from typing import List


class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        res = []
        c2n = {
            'a': '2', 'b': '2', 'c': '2',
            'd': '3', 'e': '3', 'f': '3',
            'g': '4', 'h': '4', 'i': '4',
            'j': '5', 'k': '5', 'l': '5',
            'm': '6', 'n': '6', 'o': '6',
            'p': '7', 'q': '7', 'r': '7', 's': '7',
            't': '8', 'u': '8', 'v': '8',
            'w': '9', 'x': '9', 'y': '9', 'z': '9',
        }
        for word in words:
            hit = True
            for c, n in zip(word, num):
                if c2n[c] != n:
                    hit = False
                    break
            if hit:
                res.append(word)
        return res


if __name__ == '__main__':
    cases = [
        ("8733", ["tree", "used"], ["tree", "used"]),
        ("2", ["a", "b", "c", "d"], ["a", "b", "c"]),
    ]
    sln = Solution()
    for num, words, golden in cases:
        res = sln.getValidT9Words(num, words)
        print(golden, res)
