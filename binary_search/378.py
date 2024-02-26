from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def count(target):
            cnt = 0
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    if matrix[i][j] <= target:
                        cnt += 1
                    else:
                        break
            return cnt

        low = matrix[0][0]
        high = matrix[-1][-1]
        while low < high:
            mid = (low+high)//2
            if count(mid) >= k:
                high = mid
            else:
                low = mid+1
        return low

print(Solution().kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))