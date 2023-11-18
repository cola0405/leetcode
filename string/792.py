# 暴力双指针超时
# 利用map优化匹配时的指针右移


from typing import List
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def sub(word):
            j = 0
            for i in range(len(word)):
                if j == len(s):
                    return False

                if word[i] != s[j]:
                    if word[i] not in nxt[i]:
                        return False
                    j = nxt[i][word[i]]
                j += 1
            return True

        # build map
        nxt = []
        for i in range(len(s)):
            d = dict()
            for j in range(i+1, len(s)):
                if s[j] not in d:
                    d[s[j]] = j
            nxt.append(d)

        ans = 0
        for w in words:
            if sub(w):
                ans += 1
        return ans

print(Solution().numMatchingSubseq("rwpddkvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvjubjgloeofnpjqlkdsqvruvabjrikfwronbrdyyjnakstqjac", ["wpddkvbnn","lnagtva","kvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvju","rwpddkvbnnugln","gloeofnpjqlkdsqvruvabjrikfwronbrdyyj","vbgeinupkvgmgxeaaiuiyojmoqkahwvbpwugdainxciedbdkos","mspuhbykmmumtveoighlcgpcapzczomshiblnvhjzqjlfkpina","rgmliajkiknongrofpugfgajedxicdhxinzjakwnifvxwlokip","fhepktaipapyrbylskxddypwmuuxyoivcewzrdwwlrlhqwzikq","qatithxifaaiwyszlkgoljzkkweqkjjzvymedvclfxwcezqebx"]))