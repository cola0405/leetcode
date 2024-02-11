from typing import List
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        import copy
        tmp = copy.deepcopy(mat)
        for i in range(len(mat)):
            d = mat[i][:]*2
            if i%2 == 0:
                start = k % len(mat[i])
                mat[i] = d[start: start+len(mat[i])]
            else:
                start = len(mat[i]) - (k%len(mat[i]))
                mat[i] = d[start: start+len(mat[i])]
        return mat == tmp