class Solution:
    def replaceDigits(self, s: str) -> str:
        chars = s[::2]
        shifts = s[1::2]
        sft_chars = [chr(ord(c) + int(s)) for c, s in zip(chars, shifts)]
        return ''.join([c+sc for c, sc in zip(chars, sft_chars)])
