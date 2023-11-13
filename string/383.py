class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        count1 = Counter(ransomNote)
        count2 = Counter(magazine)
        for ch in count1:
            if count1[ch] > count2[ch]:
                return False
        return True