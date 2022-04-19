class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        first_up = word[0] != word[0].lower()
        second_up = word[0] != word[0].lower()
        for w in word[1:]:
            up = w != w.lower()
            if not first_up and up:
                return False
            if second_up != up:
                return False
        return True
