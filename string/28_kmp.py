class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def build_next():
            nxt[0] = -1
            i = 0
            j = -1
            while i<len(needle):
                while j >=0 and needle[i] != needle[j]:
                    j = nxt[j]
                i += 1
                j += 1
                nxt[i] = j

        nxt = [0]*(len(needle)+1)
        build_next()

        # kmp
        i = 0
        j = 0
        while i<len(haystack):
            while j>=0 and haystack[i] != needle[j]:
                j = nxt[j]
            i += 1
            j += 1
            if j == len(needle):
                return i-j
        return -1

print(Solution().strStr(haystack = "leetcode", needle = "leeto"))
