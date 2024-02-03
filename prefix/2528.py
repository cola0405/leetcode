# prefix + binary search + difference + greedy

# after transform the power, we can find out build a new station is actually interval update
# we can use difference to optimize it
# it's hard to calculate the shortest power
# so we need to switch the perspective -- for optimization problem we have to consider the 'binary search'
# binary search the upper bound -- to make the low as large as possible

from typing import List
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        def fit(bound):
            d = diff[::]
            remain = k
            cur = 0
            for i in range(n):
                cur += d[i]
                if cur+remain < bound:
                    return False
                gap = max(0, bound-cur)     # if cur > bound -- don't need to build the new station
                if gap == 0:
                    continue
                # greedy -- build station right-most -- i+r
                if i+2*r+1 < n:     # the update of difference
                    d[i+2*r+1] -= gap
                cur += gap
                remain -= gap
            return True

        # transform to get the power
        n = len(stations)
        pre = [0]
        for num in stations:
            pre.append(pre[-1]+num)
        power = stations[::]
        for i in range(1,n+1):      # bidirectional prefix sum to calculate the current power
            power[i-1] += (pre[i-1]-pre[max(0,i-r-1)]) + (pre[min(n,i+r)]-pre[i])

        # for interval update -- we need to build the difference array to optimize it
        diff = [power[0]]
        for i in range(1, n):
            diff.append(power[i] - power[i-1])

        # binary search
        low = min(power)
        high = low + k
        while low < high:
            mid = (low+high+1)//2  # upper bound
            if fit(mid):
                low = mid
            else:
                high = mid-1
        return low

print(Solution().maxPower(stations = [1,0,1], r = 0, k = 0))