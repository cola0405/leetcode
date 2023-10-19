# 灵活使用sort和列表的比较规则

from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        count = Counter(words)
        return sorted(count, key=lambda word: (-count[word], word))[:k]

print(Solution().topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))
