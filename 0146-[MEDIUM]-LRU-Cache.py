class ListNode:
    def __init__(self, key=-1, value=None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        # For constant time lookups
        self.map = {}
        self.capacity = capacity
        # Use doubly linked-list to model LRU queue
        # Head = most recently used
        self.head = ListNode()
        # Tail = least recently used
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        # Update pos in LRU queue
        self.pop(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # Update node value
        if key in self.map:
            node = self.map[key]
            node.val = value
            # Update position in LRU queue
            self.pop(node)
            self.insert(node)
        # Need to insert new node
        else:
            # Remove LRU node if at capacity
            if len(self.map) == self.capacity:
                toRemove = self.tail.prev
                self.map.pop(toRemove.key)
                self.pop(toRemove)

            # Init new node
            node = ListNode(key, value)
            self.map[key] = node
            self.insert(node)

    # Inserts given node at head of DLL
    def insert(self, node: ListNode) -> None:
        l, r = self.head, self.head.next
        l.next = node
        node.next = r
        r.prev = node
        node.prev = l

    # Pops specified node from DLL
    def pop(self, node: ListNode) -> None:
        l, r = node.prev, node.next
        l.next = r
        r.prev = l


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
