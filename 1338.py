from typing import List
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        def frequencySort(nums):
            from collections import defaultdict
            count = defaultdict(int)
            for num in nums:
                count[num] += 1
            frequency = [(num, count[num]) for num in count]
            frequency.sort(key=lambda item: item[1], reverse=True)

            return frequency

        frequency = frequencySort(arr)
        amount = 0
        for i in range(len(frequency)):
            num, count = frequency[i]
            amount += count
            if amount >= len(arr)//2:
                return i+1

print(Solution().minSetSize(arr = [9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]))
