# binary search + preprefix sum
from typing import List
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        def count(x):
            # search how many numbers smaller than x in 2d sorted array
            cnt = 0
            j = 1
            for i in range(n):
                # prefix should include the j == n
                # lower bound but also count the same numbers
                while j <= n and pre[j] - pre[i] <= x:
                    j += 1
                cnt += j-i-1
            return cnt

        def pre_sum(k):
            # binary search the kth small number
            low = 0
            high = pre[-1]
            while low < high:       # lower bound
                mid = (low+high)//2
                if count(mid) >= k:
                    high = mid
                else:
                    low = mid+1
            k_small = low

            # get sum
            res = 0
            cnt = 0
            j = 1
            for i in range(n):
                while j <= n and pre[j]-pre[i] < k_small:
                    j += 1
                j -= 1
                res += prepre[j] - prepre[i] - pre[i]*(j-i)
                cnt += j-i
            # add numbers that equal to kth small number
            return res + k_small*(k-cnt)

        MOD = int(1e9+7)
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)
        prepre = [0]
        for num in pre[1:]:
            prepre.append(prepre[-1] + num)
        return (pre_sum(right) - pre_sum(left-1)) % MOD

print(Solution().rangeSum([7,5,8,5,6,4,3,3],8,2,6))



