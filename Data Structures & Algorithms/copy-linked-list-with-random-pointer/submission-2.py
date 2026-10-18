"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Map each old node to its new copy.
        # None maps to None, so we never need an if for null pointers.
        old_to_new = {None: None}

        # Pass 1: create a new node for every old node.
        # Only copy the value. Do not connect any pointers yet,
        # because random may point to a node that is not created yet.
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        # Pass 2: connect next and random on the new nodes.
        # Look up the old pointer in the map to get the new node.
        cur = head
        while cur:
            old_to_new[cur].next = old_to_new[cur.next]
            old_to_new[cur].random = old_to_new[cur.random]
            cur = cur.next  # move forward, or the loop never ends

        # key:old head.value:new head.
        return old_to_new[head]