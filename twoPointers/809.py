from typing import List
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def match(word):
            if len(word) > len(s):
                return False
            i = j = 0
            while j<len(word):
                cnt1 = 0
                while i<len(s) and s[i]==word[j]:
                    cnt1 += 1
                    i += 1
                last = word[j]
                cnt2 = 0
                while j<len(word) and word[j]==last:
                    cnt2 += 1
                    j += 1
                if cnt2>cnt1 or (cnt2<cnt1 and cnt1<3):
                    return False  # cnt2 is shorter and make sure cnt1 >= 3
            return i==len(s)    # check full match

        ans = 0
        for w in words:
            if match(w):
                ans += 1
        return ans


print(Solution().expressiveWords(s="abcd", words=["abc"]))
