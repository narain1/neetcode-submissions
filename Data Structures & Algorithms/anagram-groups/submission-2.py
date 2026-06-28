class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        acc = defaultdict(list)
        for s in strs:
            l = [0] * 26
            for c in s:
                l[ord(c) - ord('a')] += 1
            acc[tuple(l)].append(s)
        return [v for k, v in acc.items()]
            