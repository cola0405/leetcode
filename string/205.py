# 字典的滚动更新

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        record = dict()
        for i in range(len(s)):
            if s[i] in record:
                if record[s[i]] != t[i]:
                    return False
            else:
                record[s[i]] = t[i]
                # 题目不允许多对一
                if len(set(record.values())) != len(record.values()):
                    return False
        return True
