class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        resstr = ""

        for idx in range(len(s)):

            l, r = idx, idx
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res:
                    res = r - l + 1
                    residx = l
                l -= 1
                r += 1

            l, r = idx, idx + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res:
                    res = r - l + 1
                    residx = l
                l -= 1
                r += 1

        return s[residx: residx + res]