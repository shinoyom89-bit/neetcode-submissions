class Nodes:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash = {}
        self.left, self.right = Nodes(0, 0), Nodes(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next
        
    def get(self, key: int) -> int: 
        if key in self.hash:
            self.remove(self.hash[key])
            self.insert(self.hash[key])
            return self.hash[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.remove(self.hash[key])
            self.hash[key].val = value
            self.insert(self.hash[key])
        else:
            node = Nodes(key, value)
            self.hash[key] = node
            self.insert(node)
            if len(self.hash) > self.cap:
                lru = self.left.next
                self.remove(lru)
                del self.hash[lru.key]