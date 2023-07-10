# set去重+sort贪心


from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False

        cards = list(set(hand))
        cards.sort()

        from collections import defaultdict
        count = defaultdict(int)
        for card in hand:
            count[card] += 1

        for i in range(len(cards)-groupSize+1):
            first_card = cards[i]
            min_count = count[first_card]  # min_count skip优化
            if min_count == 0:  # 当前手牌消耗光了则跳过
                continue
            # 获取连续区间的min_count
            for j in range(1,groupSize):
                min_count = min(count[cards[i]+j], min_count)

            # update the count
            for j in range(groupSize):
                count[cards[i]+j] -= min_count

            # min_count必定消耗光区间中的其中一种牌
            # 如果first_card没消耗到0的话，必定无法连续组合
            if count[first_card] != 0:
                return False
        return max(count.values()) == 0  # 都消耗光

print(Solution().isNStraightHand([1,2,3,6,2,3,4,7,8],
3))



