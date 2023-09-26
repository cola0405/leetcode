from typing import List
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        image = [line[::-1] for line in image]
        for i in range(n):
            for j in range(n):
                image[i][j] ^= 1
        return image

print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))