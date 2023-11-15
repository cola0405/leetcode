from typing import List
from collections import defaultdict
class Trie:
    def __init__(self):
        self.child = defaultdict(Trie)
        self.word = ''

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.child[c]
        cur.word = word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def dfs(t, word, j):
            if t.word != '':
                return t.word

            if j >= len(word) or word[j] not in t.child:
                return word

            return dfs(t.child[word[j]], word, j+1)


        # build Trie
        trie = Trie()
        for root in dictionary:
            trie.insert(root)

        sentence = sentence.split()
        for i in range(len(sentence)):
            sentence[i] = dfs(trie, sentence[i], 0)

        return ' '.join(sentence)


print(Solution().replaceWords(["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))


