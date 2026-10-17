# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. 快慢指针找中点，切成两半,make sure first portion is lager
        fast, slow = head.next, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        second = slow.next
        slow.next = None
        # 2. 翻转后半段
        pre = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        # second head: pre
        # 3. 交替拼接：前1 后1 前2 后2 ...
        l, r = head, pre
        while r:
            t1, t2 = l.next, r.next
            l.next = r
            r.next = t1
            l, r = t1, t2