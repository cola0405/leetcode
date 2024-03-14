# heap iteration + greedy
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        import heapq
        pq = [-a,-b,-c]
        heapq.heapify(pq)
        ans = 0
        while len(pq) >= 2:     # take the maximum pile
            s1 = heapq.heappop(pq) * -1
            s2 = heapq.heappop(pq) * -1
            ans += 1
            s1 -= 1
            s2 -= 1
            if s1 > 0:
                heapq.heappush(pq, -s1)
            if s2 > 0:
                heapq.heappush(pq, -s2)
        return ans

print(Solution().maximumScore(2,4,6))
