class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Map key -> Node
        
        # Initialize dummy boundary nodes
        self.head = Node()
        self.tail = Node()
        
        # Wire them to point to each other initially
        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper: Detach a node completely from its current neighbors
    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node

    # Helper: Insert a node right after the dummy head (MRU side)
    def _add_to_head(self, node: Node):
        first_node = self.head.next
        
        self.head.next = node
        node.prev = self.head
        
        node.next = first_node
        first_node.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
            
        node = self.cache[key]
        # Since it was accessed, move it to the head (MRU)
        self._remove(node)
        self._add_to_head(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing key's value and move to head
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_head(node)
        else:
            # Create a brand new item
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            
            # Check if cache is full
            if len(self.cache) > self.capacity:
                # Evict the real node right before dummy tail (LRU)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]