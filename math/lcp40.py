from typing import List
class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        n = len(cards)
        cards.sort()
        seg = cards[-cnt:]
        total = sum(seg)
        if total%2 == 0:
            return total
        else:
            min_odd = float('inf')
            for i in range(len(seg)):
                if seg[i]%2 == 1:
                    min_odd = seg[i]
                    break

            min_even = float('inf')
            for i in range(len(seg)):
                if seg[i]%2 == 0:
                    min_even = seg[i]
                    break

            max_even = 0
            for i in range(n-cnt)[::-1]:
                if cards[i]%2 == 0:
                    max_even = cards[i]
                    break
            max_odd = 0
            for i in range(n-cnt)[::-1]:
                if cards[i]%2 == 1:
                    max_odd = cards[i]
                    break
            ans = 0
            if max_even != 0:
                p1 = total-min_odd+max_even
                if p1%2==0:
                    ans = max(ans, p1)

            if max_odd != 0:
                p2 = total-min_even+max_odd
                if p2%2 == 0:
                    ans = max(ans, p2)
        return ans


print(Solution().maxmiumScore(cards = [1,3,4,5], cnt = 4))