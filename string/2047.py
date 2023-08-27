class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        symbol = ['!', '.', ',']

        ans = 0
        for word in words:
            invalid = 0
            # check number
            for num in range(10):
                if str(num) in word:
                    invalid = 1
                    break

            if invalid:
                continue

            # check -
            dash_count = word.count('-')
            if dash_count == 1:
                dash_index = word.index('-')
                if dash_index == 0 or dash_index == len(word) - 1:
                    continue
                pre = word[dash_index - 1]
                after = word[dash_index + 1]
                invalid = 1
                if pre.isalpha() and after.isalpha():
                    invalid = 0
                if invalid:
                    continue
            elif dash_count>1:
                continue


            # check symbol
            for s in symbol:
                if s in word and word.index(s)!=len(word)-1:
                    invalid = 1
                    break
            if invalid:
                continue
            ans += 1

        return ans

print(Solution().countValidWords("!this  1-s b8d!"))

