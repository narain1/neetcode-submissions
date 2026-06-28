class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            word = ''.join(sorted(s))
            d[word].append(s)
        return d.values()
