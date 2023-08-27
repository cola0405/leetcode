# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []
        p = head
        while p:
            s.append(str(p.val))
            p = p.next
        s = ''.join(s)
        return s == s[::-1]
