# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 双指针 + dummy 节点，让两个指针之间固定隔 n 步
        # left 正好在要删节点的前一个

        dummy = ListNode(next = head)
        l, r = dummy, dummy
        for i in range(n):
            r = r.next
        while r.next:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next