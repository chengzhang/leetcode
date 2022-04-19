from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ln_chars = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        char_2_ln = {char: ln for ln, line in enumerate(ln_chars) for char in line}

        def same_line(w):
            w = w.lower()
            for c in w:
                if char_2_ln[c] != char_2_ln[w[0]]:
                    return False
            return True

        res = [w for w in words if w and same_line(w)]
        return res


if __name__ == '__main__':
    cases = [
        (["Hello","Alaska","Dad","Peace"], ["Alaska","Dad"]),
        (['omk'], []),
        (["adsdf","sfd"], ["adsdf","sfd"]),
    ]
    sln = Solution()
    for words, golden in cases:
        res = sln.findWords(words)
        print(golden, res)
        assert golden == res
