class Nodes():
    def __init__(self,key,value):
        self.key,self.value=key,value
        self.next=self.prev=None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.left=self.right=Nodes(0,0)
        self.left.next,self.right.prev=self.right,self.left
        self.hash={}
    def remove(self,node): #connection braker
        prev,next_node=node.prev,node.next
        prev.next,next_node.prev=next_node,prev
    def insert(self, node):
        prev, next_node = self.right.prev, self.right
    
        # 1. Wire the new node to its neighbours
        node.prev = prev
        node.next = next_node
    
        # 2. Update the surrounding nodes to point to the new node
        prev.next = node
        next_node.prev = node   
    def get(self, key: int) -> int: 
        if key in self.hash:
            self.remove(self.hash[key]) # link broker 
            self.insert(self.hash[key]) # link maker to right
            return self.hash[key].value
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.remove(self.hash[key]) # broke the link
        self.hash[key]=Nodes(key,value)
        self.insert(self.hash[key]) # link to right
        if len(self.hash)>self.capacity:
            lru=self.left.next
            self.remove(lru) # broke the link node
            del self.hash[lru.key]
