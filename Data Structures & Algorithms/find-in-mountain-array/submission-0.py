class Solution:
    def get(self, mountainArr, k):
        if k in self.cache:
            return self.cache[k]
        else:
            val = mountainArr.get(k)
            self.cache[k] = val
            return val

    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 0, mountainArr.length()
        self.cache = {}
        while l < r:
            m = (l + r) // 2
            if self.get(mountainArr, m - 1) < self.get(mountainArr, m):
                l = m + 1
            else:
                r = m

        peak = m
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            if self.get(mountainArr, m) == target:
                return m
            elif self.get(mountainArr, m) < target:
                l = m + 1
            else:
                r = m - 1
        
        l, r = peak, mountainArr.length()
        while l <= r:
            m = (l + r) // 2
            if self.get(mountainArr, m) == target:
                return m
            elif self.get(mountainArr, m) > target:
                l = m + 1
            else:
                r = m - 1
        return -1 

        
        
        