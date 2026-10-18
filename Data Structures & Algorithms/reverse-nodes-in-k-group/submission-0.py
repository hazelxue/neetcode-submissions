# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #1.length of lists
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        dummy = ListNode(next = head)
        # head node
        p0 = dummy
        # for every k node
        pre = None
        cur = p0.next

        while n >= k:
            n -= k

            for i in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            
            tmp = p0.next
            # remember the 2 lines need connect
            p0.next.next = cur
            p0.next = pre
            p0 = tmp
            pre = None

        return dummy.next

