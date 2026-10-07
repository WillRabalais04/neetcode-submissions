class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        ret = 1
        for i in range(1, abs(n) + 1):
            ret *= x
        return ret if n > 0 else (1.0 / ret)

            



        