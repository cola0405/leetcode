class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        count[s[0]] += 1
        cur_len = 1
        # 以当前s[i]结尾的最长的字串的长度就是种类数
        # 直接就不用考虑重复的问题。。。
        for i in range(1,len(s)):
            # 重置字符串的条件 -- 在环下不连续，即可剪枝重置了
            if ord(s[i])-1 != ord(s[i-1]) and not (s[i]=='a' and s[i-1] == 'z'):  # 判断成串的条件
                cur_len = 0
            cur_len += 1
            count[s[i]] = max(cur_len, count[s[i]])
        return sum(count.values())

print(Solution().findSubstringInWraproundString("zab"))