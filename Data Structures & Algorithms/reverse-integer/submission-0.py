class Solution:
    def reverse(self, x: int) -> int:
        def rec(n):
            rev = 0
            while n > 0:
                rev = rev * 10 + n % 10
                n //= 10
            return rev
         
        sign = -1 if x < 0 else 1
        x = abs(x)
        reverse_num = rec(x)
        reverse_num *= sign
        if reverse_num < -(1 << 31) or reverse_num > (1 << 31) - 1:
            return 0
        return reverse_num