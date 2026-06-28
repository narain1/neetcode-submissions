class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # d = defaultdict(int, 0)
        d = {}
        d1 = {}
        for a in s:
            if a in d:
                d[a] += 1
            else:
                d[a] = 1

        for a in t:
            if a in d1:
                d1[a] += 1
            else:
                d1[a] = 1
        return d1 == d

            
