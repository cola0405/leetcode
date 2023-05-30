class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w = ''
        ans = 0
        for ch in s:
            if ch not in w:
                w += ch
            else:
                idx = w.find(ch)
                ans = max(len(w), ans)
                w = w[idx+1:]+ch
        return max(len(w), ans)

print(Solution().lengthOfLongestSubstring(s = " "))
