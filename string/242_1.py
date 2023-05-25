class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {chr(i): 0 for i in range(97,123)}
        for ch in s:
            count[ch] += 1
        for ch in t:
            count[ch] -= 1
            if count[ch] < 0:  # 数据量大的话还是剪枝划算
                return False

        for ch in count:
            if count[ch] != 0:
                return False
        return True


