# binary search + greedy + the Sieve of Eratosthenes algorithm

from typing import List
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        n = max(nums)
        is_prime = [True] * (n+1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p*p, n+1, p):
                    is_prime[i] = False
            p += 1
        prime = [num for num in range(2, n+1) if is_prime[num]]

        for i in range(len(nums)-1)[::-1]:
            # binary search the prime > (nums[i] - nums[i+1]) -- lower bound
            target = nums[i] - nums[i+1]
            if target >= 0:
                low = 0
                high = len(prime)-1
                while low < high:
                    mid = (low+high)//2
                    if prime[mid] > target:
                        high = mid
                    else:
                        low = mid+1
                nums[i] -= prime[low]
                if nums[i] >= nums[i+1] or nums[i] <= 0:
                    return False
        return True

print(Solution().primeSubOperation([5,8,3]))
