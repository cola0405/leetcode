from typing import List
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for num in range(1,len(arr)+1)[::-1]:
            idx = arr.index(num)

            if idx+1 != num:
                if arr[0] != num:
                    ans.append(idx + 1)
                    arr[:idx+1] = arr[:idx+1][::-1]
                ans.append(num)
                arr[:num] = arr[:num][::-1]
        return ans

print(Solution().pancakeSort([3,2,4,1]))
