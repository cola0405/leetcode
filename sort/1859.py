class Solution:
    def sortSentence(self, s: str) -> str:
        words = sorted([(int(word[-1]), word[:-1]) for word in s.split()])
        return ' '.join([word for rank,word in words])

print(Solution().sortSentence("is2 sentence4 This1 a3"))

