class Solution:
    def customSortString(self, order: str, s: str) -> str:
        from collections import Counter
        count = Counter(s)

        ans = ''
        for ch in order:
            ans += ch * count[ch]
            count[ch] = 0

        for ch in count:
            if count[ch] != 0:
                ans += ch * count[ch]

        return ans