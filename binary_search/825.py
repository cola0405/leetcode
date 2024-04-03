# sort + binary search

# find the pattern
# reverse the condition
# the x will only send the request to y
# which is younger and fit the condition y > 0.5x + 7
# it's actually a group of people just next to x

# there do have a special situation -- [16,16]
# in some situation x == y, people will also send request to the right

from typing import List
from collections import Counter
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def bound(inx):
            low = 0
            high = inx
            x = ages[inx]
            while low < high:
                mid = (low+high)//2
                y = ages[mid]
                if y <= x and y > 0.5*x + 7:
                    high = mid
                else:
                    low = mid+1
            return low

        n = len(ages)
        cnt = Counter(ages)
        ages.sort()
        ans = 0
        for i in range(n):
            # deal with the requests to the right
            if ages[i] > 0.5*ages[i]+7:
                ans += cnt[ages[i]]*(cnt[ages[i]]-1)//2
                cnt[ages[i]] = 0    # clean
            ans += i-bound(i)
        return ans

print(Solution().numFriendRequests([16,16]))