class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # initialize lrucache
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        # double linked list, search and insert: O(1)
        self.head = Node()
        self.tail = Node()
        # head ⇄ tail
        # head ⇄ [k1] ⇄ [k2] ⇄ [k3] ⇄ tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # two helper methods
    def _remove(self, node):#2 operations
        node.prev.next = node.next
        node.next.prev = node.prev
    def _add_to_head(self, node):#4 operations
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    # hash → linked list  → remove to head
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_head(node)
        return node.val
        
    # if put exist: remove old node, add new node to head, check if out of capacity(remove tail node)
    # if not exist: add...
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
            # Delete a key from a dictionary
            del self.cache[key]
        node = Node(key, value)
        self.cache[key] = node
        self._add_to_head(node)
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            # this method need key because: from node to key
            del self.cache[lru.key]

        
