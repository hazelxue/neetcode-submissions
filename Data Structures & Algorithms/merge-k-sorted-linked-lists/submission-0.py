# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge2list(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # forget
        if not lists:
            return None

        merge = lists
        while len(merge) > 1:
            level = []
            # avoid out of range
            for i in range(0, len(merge), 2):
                l1 = merge[i]
                l2 = merge[i + 1] if i + 1 < len(merge) else None
                level.append(self.merge2list(l1, l2))
            merge = level
        return merge[0]
    
