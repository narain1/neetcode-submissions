class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = defaultdict(list)
        for s in strs:
            count = Counter(s)
            semantic_count = [0] * 26
            for k, v in count.items():
                semantic_count[ord(k) - ord('a')] += v
            
            keys[','.join(map(str, semantic_count))].append(s)

        return list(keys.values())