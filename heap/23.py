# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ListNode.__lt__ = lambda a,b: a.val < b.val
from typing import List, Optional
from heapq import *
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = [node for node in lists if node]
        heapify(pq)
        cur = head = ListNode()
        while pq:
            top = heappop(pq)
            if top.next:
                heappush(pq, top.next)
            cur.next = top
            cur = top
        return head.next

print(Solution().mergeKLists())
