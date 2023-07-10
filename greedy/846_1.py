# sort贪心 + hash表优化查找空间
from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False

        from collections import defaultdict
        count = defaultdict(int)
        for card in hand:
            count[card] += 1
        hand.sort()
        for card in hand:
            if count[card] == 0:  # 当前手牌消耗光了则跳过
                continue

            for j in range(groupSize):
                count[card+j] -= 1  # hash表优化查找
                if count[card+j]<0:
                    return False
        return True

print(Solution().isNStraightHand([2,1],
2))



