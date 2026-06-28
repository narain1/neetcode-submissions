class ListNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]

    def hash(self, key):
        return key % 1000

    def put(self, key: int, value: int) -> None:
        ptr = self.map[self.hash(key)]
        while ptr.next:
            if ptr.next.key == key:
                ptr.next.val = value
                return
            ptr = ptr.next
        ptr.next = ListNode(key, value)

        

    def get(self, key: int) -> int:
        ptr = self.map[self.hash(key)]
        while ptr:
            if ptr.key == key:
                return ptr.val
            ptr = ptr.next
        return -1

    def remove(self, key: int) -> None:
        ptr = self.map[self.hash(key)]
        while ptr and ptr.next:
            if ptr.next.key == key:
                ptr.next = ptr.next.next
            ptr = ptr.next
        return
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)