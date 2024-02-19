# pre-sort make sure the order

from typing import List
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        cur = products
        ans = []
        for i in range(len(searchWord)):
            remain = []
            for j in range(len(cur)):
                if i < len(cur[j]) and searchWord[i] == cur[j][i]:
                    remain.append(cur[j])
            ans.append(remain[:3])
            cur = remain
        return ans

print(Solution().suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"))