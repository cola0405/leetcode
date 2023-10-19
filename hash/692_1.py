# 学会排序

from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        count = [(word, amount) for word, amount in Counter(words).items()]
        n = len(count)

        for i in range(k):
            max_idx = i
            for j in range(i,n):
                if count[j][1] > count[max_idx][1]:
                    max_idx = j
                elif (count[j][1] == count[max_idx][1]
                      and count[j][0]<count[max_idx][0]):
                    max_idx = j
            count[i], count[max_idx] = count[max_idx], count[i]
        return [item[0] for item in count[:k]]

print(Solution().topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))
