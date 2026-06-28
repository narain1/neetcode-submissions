class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lfu_count = 0
        self.val_map = {}
        self.count_map = defaultdict(int)
        self.list_map = defaultdict(deque)
        
    def counter(self, key):
        count = self.count_map[key]
        self.count_map[key] += 1
        if count > 0:
            if key in self.list_map[count]:
                self.list_map[count].remove(key)
        self.list_map[count + 1].append(key)
        if count == self.lfu_count and not self.list_map[count]:
            self.lfu_count += 1

    def get(self, key):
        if key not in self.val_map: return -1
        self.counter(key)
        return self.val_map[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return

        if key not in self.val_map and len(self.val_map) == self.capacity:
            removed_key = self.list_map[self.lfu_count].popleft()
            self.val_map.pop(removed_key)
            self.count_map.pop(removed_key)
        
        self.val_map[key] = value
        self.counter(key)
        self.lfu_count = min(self.lfu_count, self.count_map[key])

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)