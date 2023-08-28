# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        stack = []
        p = head
        while p:
            stack.append(ListNode(p.val, p.next))  # p会有引用问题
            p = p.next

        head = stack.pop()
        cur = head
        while stack:
            top = stack.pop()
            cur.next = top
            cur = top

        cur.next = None  # 解环
        return head


