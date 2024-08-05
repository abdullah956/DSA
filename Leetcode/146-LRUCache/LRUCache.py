class Node : #doubly linked list
    def __init__(self, key, val) : #node constructor will have key value 
        self.key , self.val = key , val
        self.prev = self.next = None 
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity #just to get total capacity of cache
        self.cache = {} #map key val node 
        #left is LRU and right is most recent used
        self.left , self.right = Node(0,0) , Node(0,0)
        #nodes will be inserted btw them so they will be connected from default
        self.left.next , self.right.prev = self.right , self.left
    def remove(self, node: Node) -> None :
        #prev is the node before the node to be deleted 
        #nxt is the node next to be deleetd node 
        prev , nxt = node.prev , node.next
        #prev.next will point to next
        #nxt.prev will point to prev
        #thus deleting the node in between
        prev.next , nxt.prev = nxt , prev
    def insert(self, node: Node) -> None :
        #new node wil be inserted before right which is our end node
        #so prev is the second last node 
        #and nxt is the last node
        prev , nxt = self.right.prev , self.right
        #prev.next and nxt.prev will point to node 
        #thus insertng the node in between
        prev.next = nxt.prev = node
        #just connecting the node with prev and nxt
        node.next , node.prev = nxt , prev
    def get(self, key: int) -> int:
        #first checking if the key is in our cache
        if key in self.cache :
            #removing the asked key from the doubly linked list
            #then puttinh it at the very end
            #beacuse the most recent key asked (cache) will be at the very end 
            #before thr right node
            self.remove(self.cache[key]) 
            self.insert(self.cache[key])
            #after that just returning that key value
            return self.cache[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        #if key already present remove it because we are going to add the new key 
        if key in self.cache :
            self.remove(self.cache[key])
        #making new node in map with key value
        self.cache[key] = Node(key,value)
        #then just inserting the node in doubly linked list
        self.insert(self.cache[key])
        #now we also have to check the limit (capacity of the caceh)
        if len(self.cache) > self.cap :
            #delete the LRU which will be next to left if we exceed our capacity
            LRU = self.left.next
            self.remove(LRU)
            #now just delete the node from the map
            del self.cache[LRU.key]
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""
class Node : 
    def __init__(self, key: int, val: int) :
        self.key , self.val = key , val
        self.prev = self.next = None 
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {} 
        self.left , self.right = Node(0,0) , Node(0,0)
        self.left.next , self.right.prev = self.right , self.left
    def remove(self, node: Node) -> None :
        prev , nxt = node.prev , node.next
        prev.next , nxt.prev = nxt , prev
    def insert(self, node: Node) -> None:
        prev , nxt = self.right.prev , self.right
        prev.next = nxt.prev = node
        node.next , node.prev = nxt , prev
    def get(self, key: int) -> int:
        if key in self.cache :
            self.remove(self.cache[key]) 
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache :
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap :
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
"""