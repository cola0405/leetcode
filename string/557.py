class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([seg[::-1] for seg in s.split()])