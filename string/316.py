class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import defaultdict
        count = {ch:1 for ch in s}
        for ch in s:
            count[ch] = 1
        print(count)
        return ''.join([ch for ch in count])

print(Solution().removeDuplicateLetters(s = "cbacdcbc"))