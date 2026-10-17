# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        second = slow.next
        slow.next = None

        pre = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        # second head: pre
        l, r = head, pre
        while r:
            t1, t2 = l.next, r.next
            l.next = r
            r.next = t1
            l, r = t1, t2