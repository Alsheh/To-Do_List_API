class Node:
    def __init__(self, v):
        self.val = v
        self.prev = None
        self.next = None

class Cache:
    '''
    Cache is implemented using (Linked list + hashtable) to allow:
        1. O(1) insertion
        2. O(1) removal
        3. O(1) look up
        4. O(1) retrieval
        5. Keeping nodes in the order in which they are added.
    '''
    def __init__(self):
        self.dic = dict()
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            return self.dic[key]
        return -1

    def put(self, key, value):
        n = Node(value)
        self._add(n)
        self.dic[key] = n

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    def contains(self, key):
        if key in self.dic:
            return True
        else:
            return False

    def remove(self, key):
        if key not in self.dic:
            return -1
        node = self.dic[key]
        del self.dic[key]
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

        
class TaskCache(Cache):
    def toList(self, allowedTypes=[]):
        res = []
        node = self.head.next
        while node.val != 0:
            if node.val.type in allowedTypes:
                res.append(node.val)
            node = node.next
        return res
    
