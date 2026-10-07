class Solution:
    def isHappy(self, n: int) -> bool:

        def SOSGEN(num):
            arr = list(str(num))
            SOS = 0
            for num in arr:
                SOS += int(num) ** 2
            return SOS

        seen = defaultdict(bool)
        
        while True:
            seen[n] = True
            SOS = SOSGEN(n)
            if SOS == 1:
                return True
            if seen[SOS]:
                return False
            n = SOS
            


