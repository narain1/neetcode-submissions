class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count('1')
        res = 0
        for i in range(32):
            res += n % 2
            n >>= 1
        return res