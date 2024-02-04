# 二分找子串

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def get_sub(l):
            already = set()
            for i in range(len(s)-l+1):
                seg = s[i:i+l]
                if seg in already:
                    return seg
                else:
                    already.add(seg)
            return ''

        low = 0
        high = len(s)-1

        ans = ''
        while low<high:
            mid = (low+high+1)//2
            res = get_sub(mid)  # 因为题目要具体的子串
            if len(res)>0:
                low = mid
                ans = res
            else:
                high = mid-1
        return ans

print(Solution().longestDupSubstring("banana"))
