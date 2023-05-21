class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {ch: 0 for ch in s}
        for ch in s:
            d[ch] += 1
        for k in d:
            if d[k] == 1:
                return s.index(k)
        return -1
