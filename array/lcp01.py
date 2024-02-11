from typing import List
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        ans = 0
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                ans += 1
        return ans