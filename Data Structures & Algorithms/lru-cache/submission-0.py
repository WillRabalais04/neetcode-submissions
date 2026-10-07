class Node:
    def __init__(self, key, val):
        self.key= key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        p,n = node.prev, node.next
        p.next = n
        n.prev = p

    def insert(self, node):
        p,n = self.right.prev, self.right
        p.next = n.prev = node
        node.next = n
        node.prev = p

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            x = self.left.next
            self.remove(x)
            del self.cache[x.key]


        
