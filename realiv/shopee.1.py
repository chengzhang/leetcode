"""
题目：输入一个词典和一个句子，输出分词结果。采用最大前向的分词方法：如果在词典中有匹配的，则选择切分到能匹配的最长的词，否则切出单个字。
例子：
    输入：
        词典：[你好，天气晴朗，天气，晴朗，今天，今天天气]
        句子： 主人你好呀今天天气晴朗
    输出： 主 人 你好 呀 今天天气 晴朗
"""


from typing import List


class Tokenizer(object):

    class TrieNode(object):
        def __init__(self, char=''):
            self.char = char
            self.children = {}
            self.end = False

    def __init__(self, vocab):
        self.vocab = vocab
        self.root = self.TrieNode()
        self._build()

    def _build(self):
        for w in self.vocab:
            node = self.root
            for c in w:
                if c not in node.children:
                    node.children[c] = self.TrieNode(c)
                node = node.children[c]
            node.end = True

    def _match(self, s, i) -> int:
        j = i
        node = self.root
        while i < len(s):
            if s[i] not in node.children:
                break
            node = node.children[s[i]]
            if node.end:
                j = i
            i += 1
        return j + 1

    def __call__(self, sentence) -> List[str]:
        res = []
        i = 0
        while i < len(sentence):
            j = self._match(sentence, i)
            res.append(sentence[i:j])
            i = j
        return res


tokenizer = Tokenizer(['你好', '天气晴朗', '天气', '晴朗', '今天', '今天天气'])
print(tokenizer('主人你好呀今天天气晴朗'))
