from typing import List
class Solution:
    def checkDynasty(self, places: List[int]) -> bool:
        known = []
        for d in places:
            if d != 0:
                known.append(d)
        if len(set(known)) != len(known):
            return False
        missing = 0
        for d in range(min(known), max(known)+1):
            if d not in known:
                missing += 1
        return missing <= len(places) - len(known)