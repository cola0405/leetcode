class Solution:
    def countValidWords(self, sentence: str) -> int:
        def valid(word):
            # check number
            for num in range(10):
                if str(num) in word:
                    return False

            # check -
            dash_count = word.count('-')
            if dash_count == 1:
                dash_index = word.index('-')
                if dash_index == 0 or dash_index == len(word) - 1:
                    return False

                pre = word[dash_index - 1]
                after = word[dash_index + 1]
                if pre<'a' or pre>'z' or after<'a' or after>'z':
                    return False

            elif dash_count > 1:
                return False

            # check symbol
            for s in symbol:
                if s in word and word.index(s) != len(word) - 1:
                    return False

            return True

        # main
        words = sentence.split()
        symbol = ['!', '.', ',']
        ans = 0
        for w in words:
            if valid(w):
                ans += 1
        return ans

print(Solution().countValidWords("cat and  dog"))

