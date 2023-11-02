# 直接求解难，试着转化问题
# count 小于k的一定不可选
# 那么答案肯定是在被切分的各个seg中的
# 那么其实可以用分治的方法来解题

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        from collections import Counter
        if len(s) == 0:
            return 0

        count = Counter(s)
        seg_points = [ch for ch in count if count[ch] < k]
        if len(seg_points) == 0:  # if no stop
            return len(s)

        res = 0
        seg = ''
        for i in range(len(s)):
            if s[i] not in seg_points:
                seg += s[i]
            else:
                res = max(res, self.longestSubstring(seg, k))
                seg = ''

        return max(res, self.longestSubstring(seg, k))


print(Solution().longestSubstring(s = "aaabb", k = 3))
