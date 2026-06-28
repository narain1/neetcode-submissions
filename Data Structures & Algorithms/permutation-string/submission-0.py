class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l2 < l1:
            return False

        c1 = [0] * 26
        c2 = [0] * 26

        for ci, cj in zip(s1, s2):
            c1[ord(ci) - ord('a')] += 1
            c2[ord(cj) - ord('a')] += 1

        if c1 == c2:
            return True

        for idx in range(l1, l2):
            c2[ord(s2[idx]) - ord('a')] += 1
            c2[ord(s2[idx - l1]) - ord('a')] -= 1

            if c1 == c2:
                return True

        return False


        