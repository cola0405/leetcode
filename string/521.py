# 答案肯定在较长的字符串
# 如果两个字符串一样，那就返回-1

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b)) if a != b else -1

print(Solution().findLUSlength(a = "aba", b = "cdc"))