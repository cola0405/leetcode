from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        ans = 0
        i = 0
        j = n-1
        while i <= j:
            if i == j:
                ans += 1
                break
            if i < j and people[j] + people[i] <= limit:
                i += 1      # Each boat carries at most two people
            ans += 1
            j -= 1
        return ans


print(Solution().numRescueBoats([2,49,10,7,11,41,47,2,22,6,13,12,33,18,10,26,2,6,50,10], limit = 50))

