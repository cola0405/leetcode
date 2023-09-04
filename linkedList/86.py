# stack+链表
# 考察特殊情况的处理

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = []
        large = []

        p = head
        while p:
            node = p
            if p.val < x:
                small.append(node)
            else:
                large.append(node)
            p = p.next

        # 构造small链
        small_head = None
        small_tail = None
        if len(small)>0:
            small_head = small[0]
            small_tail = small[-1]

        for i in range(len(small)-1):
            small[i].next = small[i+1]

        # 构造large链 -- x没有说一定是链表中存在的节点
        large_head = None
        large_tail = None
        if len(large)>0:
            large_head = large[0]
            large_tail = large[-1]
            large_tail.next = None # 处理尾巴

        for i in range(len(large)-1):
            large[i].next = large[i+1]

        # 连接
        if small_head:
            head = small_head
        else:
            head = large_head

        if small_tail:
            small_tail.next = large_head
        return head






