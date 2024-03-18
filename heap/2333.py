# hash-table batch iteration to get down the complexity
from typing import List
from collections import defaultdict
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        cnt = defaultdict(int)
        for i in range(len(nums1)):
            cnt[abs(nums1[i]-nums2[i])] += 1
        k = k1+k2
        gap = max(cnt.keys())   # dealing with maximum first
        while k > 0 and gap > 0:
            if k >= cnt[gap]:
                k -= cnt[gap]
                cnt[gap-1] += cnt[gap]     # can only decrease by 1
                cnt[gap] = 0
                gap -= 1
            else:
                cnt[gap-1] += k
                cnt[gap] -= k
                break
        ans = 0
        for k in cnt:
            ans += k**2 * cnt[k]
        return ans


print(Solution().minSumSquareDiff([1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1))