# 二分结合测试用例试。。
from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0
        high = len(arr)-1
        while low<high:
            mid = (low+high)//2
            missing = arr[mid]-mid-1  # 左边缺多少个
            if missing >= k:
                high = mid
            else:
                low = mid+1
        missing = arr[low]-low-1
        if missing-k < 0:
            return arr[low]+(k-missing)  # 往右边找
        return arr[low]-(missing-k+1)  # 往左边找

print(Solution().findKthPositive(arr=[3,10], k = 2))