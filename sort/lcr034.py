from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def fit(a,b):
            r = min(len(a),len(b))
            for i in range(r):
                if inx[a[i]] < inx[b[i]]:
                    return True
                elif inx[a[i]] > inx[b[i]]:
                    return False
            return len(a) < len(b)

        inx = {order[i]: i for i in range(len(order))}
        for i in range(len(words)-1):
            if not fit(words[i], words[i+1]):
                return False
        return True

print(Solution().isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))