class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # d1 = defaultdict(int)
        # d2 = defaultdict(int)
        # for a in s:
        #     d1[a] += 1

        # for a in t:
        #     d2[a] += 1
        # return d1 == d2

            
        return Counter(s) == Counter(t)