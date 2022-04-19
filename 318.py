from typing import List


class Node(object):
    def __init__(self, char, part):
        self.char = char
        self.part = part
        self.max_len = 0
        self.left = None
        self.right = None


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        app = [[False for _ in range(n)] for _ in range(26)]
        for i, w in enumerate(words):
            for c in w:
                app[ord(c)-ord('a')][i] = True

        def build_tree(part, char):
            print(' '*char, len(part))
            if not part or char == 26:
                return None
            lpart = [w for w in part if not app[char][w]]
            node = Node(char, part)
            node.left = build_tree(lpart, char+1)
            node.right = build_tree(part, char+1)
            node.max_len = max(len(words[w]) for w in part)
            return node

        def match(w, node):
            if not node:
                res = 0
            elif not node.left and not node.right:
                res = len(words[w]) * node.max_len
            elif app[node.char][w]:
                res = match(w, node.left)
            else:
                res = match(w, node.right)
            return res

        word_ids = list(range(n))
        root = build_tree(word_ids, 0)

        return max(match(w, root) for w in word_ids)

    def maxProduct_0(self, words: List[str]) -> int:
        n = len(words)
        app = [[False for _ in range(n)] for _ in range(26)]
        for i, w in enumerate(words):
            for c in w:
                app[ord(c)-ord('a')][i] = True

        def build_tree(part, char):
            if not part or char == 26:
                return None
            lpart, rpart = [], []
            for w in part:
                if app[char][w]:
                    rpart.append(w)
                else:
                    lpart.append(w)
            node = Node(char, part)
            node.left = build_tree(lpart, char+1)
            node.right = build_tree(rpart, char+1)
            node.max_len = max(len(words[w]) for w in part)
            return node

        def match(w, node):
            if not node:
                return 0
            res = match(w, node.left)
            if not app[node.char][w]:
                res = max(res, match(w, node.right))
            if not node.left and not node.right:
                res = max(res, len(words[w]) * node.max_len)
            return res

        word_ids = list(range(n))
        root = build_tree(word_ids, 0)
        print('build done')

        return max(match(w, root) for w in word_ids)


if __name__ == '__main__':
    cases = [
        (["abcw","baz","foo","bar","xtfn","abcdef"], 16),
        (["a","ab","abc","d","cd","bcd","abcd"], 4),
        (["a","aa","aaa","aaaa"], 0),
        (["abcw", "baz", "foo", "bar", "xtfn", "abcdef"], 0)
    ]
    sln = Solution()
    for words, golden in cases:
        res = sln.maxProduct(words)
        print(res, golden)
        assert res == golden
