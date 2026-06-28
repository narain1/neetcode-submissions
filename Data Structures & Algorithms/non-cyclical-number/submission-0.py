class Solution:
    def isHappy(self, n: int) -> bool:
        # x = iterative (x%10)**2; x /= 10; 
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumofsquares(n)
            if n == 1: return True
        return False

    def sumofsquares(self, n):
        s = 0
        for a in str(n):
            s += int(a)**2
        return s



            