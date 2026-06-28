class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])): # iterates of len of first word character
            for s in strs: # iterates over word
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]

