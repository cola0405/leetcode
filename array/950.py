class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        ans = []
        for num in deck:
            if len(deck) == 0:
                continue
            ans.insert(0,ans.pop())
            ans.insert(0,num)
        return ans