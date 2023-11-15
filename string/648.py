from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def successor(a, b):
            for i in range(len(a)):
                if a[i] != b[i]:
                    return False
            return True

        sentence = sentence.split()
        dictionary.sort(key=lambda item:len(item))
        for i in range(len(sentence)):
            for root in dictionary:
                if len(sentence[i]) < len(root):
                    break

                if successor(root, sentence[i]):
                    sentence[i] = root
        return ' '.join(sentence)

print(Solution().replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"))


