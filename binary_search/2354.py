# pattern discover + bit-count + binary search

# you can write the loop to print out the result to discover the pattern
# the sum of bit-count of "a&b" and "a|b" is equal to the bit-count of "a" and "b"
# so we can build a sorted array of the ones, then binary search the bound that fits
from typing import List
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        def one_cnt(x):     # count the number of 1 in binary representation
            res = 0
            while x:
                res += 1
                x &= x-1
            return res

        s = set(nums)
        ans = 0
        for num in s:       # for (num,num) -- (3,3) >= 6
            if one_cnt(num)*2 >= k:
                ans += 1

        # sort according to the bit-count
        ones = list(one_cnt(num) for num in s)
        ones.sort()

        n = len(ones)
        for i in range(n-1):
            low = i+1
            high = n-1
            while low < high:
                mid = (low+high)//2
                if ones[i] + ones[mid] >= k:
                    high = mid
                else:
                    low = mid+1

            if ones[i] + ones[low] >= k:
                ans += (n-low)*2    # mutual
        return ans

print(Solution().countExcellentPairs(nums = [1,2,3,1], k = 3))