# 字典树解决前缀问题

from typing import List
from collections import defaultdict
class Trie():
    def __init__(self):
        self.word = ''
        self.child = defaultdict(Trie)

    def insert(self, word):
        cur = self
        for ch in word:
            cur = cur.child[ch]  # defaultdict 会做Trie()
        cur.word = word


class Solution:
    def longestWord(self, words: List[str]) -> str:
        def dfs(node):
            if node.word != '*' and len(node.word) == 0:
                return

            if node.word != '*':
                nonlocal ans
                if len(node.word) > len(ans):
                    ans = node.word
                elif len(node.word) == len(ans) and node.word < ans:
                    ans = node.word

            for x in node.child:
                dfs(node.child[x])

        t = Trie()
        t.word = "*"   # 解决dfs入口问题
        for word in words:
            t.insert(word)

        ans = ''
        dfs(t)
        return ans

print(Solution().longestWord(["ts","e","x","pbhj","opto","xhigy","erikz","pbh","opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi","x","o"]))


