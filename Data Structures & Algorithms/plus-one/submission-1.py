class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ptr = len(digits) - 1
        carry = 1
        while ptr >= 0 and carry:
            digits[ptr] += carry
            carry = digits[ptr] // 10
            digits[ptr] = digits[ptr] % 10
            ptr -= 1
        if carry > 0:
            return [carry] + digits
        return digits
        