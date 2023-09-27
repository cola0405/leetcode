# 单词数量上去之后，用前缀树处理会更合适
# 不再需要每个单词都从头搜索一编，完全是碾压暴力法的。。。

# insert() 构建的前缀树
# root
# |
# ('', {'e': Trie})
#              |
#            ('', {'a': Trie})
#                         |
#                         ('', {'t':Trie})
#                                     |
#                                     ('eat', {})

# dfs搜索时，如果该节点的存了有单词，则说明该单词可构建

from collections import defaultdict
class Trie:
    def __init__(self):
        self.child = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.child[c]
        cur.word = word

from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node, row, column):
            if (row<0 or row>=m) or (column<0 or column>=n)\
                    or board[row][column] not in node.child:    # 同时也能识别标志位
                return

            ch = board[row][column]
            node = node.child[ch]

            if node.word != '':
                ans.add(node.word)  # 还要继续下去，因为除了eat，可能还会有eatter在后面

            board[row][column] = '#'

            dfs(node, row+1, column)
            dfs(node, row-1, column)
            dfs(node, row, column+1)
            dfs(node, row, column-1)

            board[row][column] = ch  # 回溯


        def get_available_letters():
            res = set()
            for row in range(m):
                for column in range(n):
                    res.add(board[row][column])
            return res

        def letter_exist(word):
            for letter in word:
                if letter not in available_letters:
                    return False
            return True

        ans = set()
        m = len(board)
        n = len(board[0])
        available_letters = get_available_letters()
        trie = Trie()
        for w in words:
            if letter_exist(w):
                trie.insert(w)

        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)
        return list(ans)


