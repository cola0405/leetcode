class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        # from collections import defaultdict
        # d1 = defaultdict(int)
        # d2 = defaultdict(int)
        # for ch in word1:
        #     d1[ch] += 1
        # for ch in word2:
        #     d2[ch] += 1
        from collections import Counter
        d1 = Counter(word1)
        d2 = Counter(word2)
        for a in d1.keys():
            for b in d2.keys():
                if a==b:  # a,b 相等时就不应该进行elif的判断了
                    if len(d1) == len(d2):
                        return True
                # len - x + y
                # 看len经过增减之后是否相等
                elif len(d1) - (d1[a]==1) + (b not in d1) == \
                     len(d2) - (d2[b]==1) + (a not in d2):
                    return True
        return False

print(Solution().isItPossible(word1 = "aa", word2 = "ab"))

