from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d = {}
        for i in range(26):
            d[chr(97+i)] = m[i]

        s = set()
        for word in words:
            res = ''
            for c in word:
                res += d[c]
            s.add(res)
        return len(s)

print(Solution().uniqueMorseRepresentations(words = ["gin", "zen", "gig", "msg"]))
