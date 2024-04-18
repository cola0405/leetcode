# topology sort + hash in_deg
from typing import List
from collections import defaultdict, deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        in_deg = defaultdict(set)   # {recipe: {ingredient}}
        for i in range(n):
            for x in ingredients[i]:
                in_deg[recipes[i]].add(x)

        q = deque(supplies)
        ans = []
        while q:    # available ingredients
            x = q.pop()
            if x in recipes:
                ans.append(x)
            for v in in_deg:    # update the in_degree
                if x in in_deg[v]:
                    in_deg[v].remove(x)
                    if len(in_deg[v]) == 0:     # no lack of ingredients
                        q.append(v)
        return ans

print(Solution().findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]))
print(Solution().findAllRecipes(recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]))