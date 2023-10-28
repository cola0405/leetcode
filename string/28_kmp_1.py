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
                # 可以优化处理AAAAAAAB这种，相邻重复元素多的
                # 一旦p[i] != p[j]，不用再去一遍一遍倒next，就是得从头开始
                # 注意观察不同的next数组
                # 优化前: nxt[i] = j
                nxt[i] = j if i<len(needle) and needle[i] != needle[j] else nxt[j]

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
