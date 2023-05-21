class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {chr(i): 0 for i in range(97,123)}
        count2 = {chr(i): 0 for i in range(97, 123)}
        for ch in s:
            count1[ch] += 1
        for ch in t:
            count2[ch] += 1

        for ch in count1:
            if count1[ch] != count2[ch]:
                return False
        return True


