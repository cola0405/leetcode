from typing import List
from collections import deque
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        uncheck_box = deque(initialBoxes)
        available_keys = set()
        found_box = set(initialBoxes)
        ans = 0
        flag = True
        while uncheck_box and flag:
            flag = False
            for k in range(len(uncheck_box)):
                i = uncheck_box.popleft()
                # try to open the box
                if status[i] or (i in available_keys and i in found_box):
                    flag = True
                    for key in keys[i]:
                        available_keys.add(key)
                    for box in containedBoxes[i]:
                        uncheck_box.append(box)
                        found_box.add(box)
                    ans += candies[i]
                else:
                    # put it back, when can't open the current box
                    uncheck_box.append(i)
        return ans

# print(Solution().maxCandies(status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]))
print(Solution().maxCandies(status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]))