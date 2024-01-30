class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper_cnt = 0
        for ch in word:
            if 'A' <= ch <= 'Z':
                upper_cnt += 1
        return upper_cnt == 0 or upper_cnt == len(word) or ('A' <= word[0] <= 'Z' and upper_cnt==1)

