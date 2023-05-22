class Solution:
    def equalFrequency(self, word: str) -> bool:
        d = {ch:0 for ch in word}
        for ch in word:
            d[ch] += 1
        for ch in d:
            d[ch] -= 1
            s = set(d.values())
            if len(s) == 1 or (d[ch] == 0 and len(s)==2):
                return True
            d[ch] += 1
        return False


print(Solution().equalFrequency(word="ddaccb"))