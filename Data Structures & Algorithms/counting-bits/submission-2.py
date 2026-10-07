class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0] * (n + 1)
        for i in range(n + 1):
            print("i: '" + str(i) + "' | i >> 1: '" + str(i >> 1) + "' | ret[i >> 1]: '" + str(ret[i >> 1]) + "' | i & 1: '" + str(i & 1) + "'")
            ret[i] = ret[i >> 1] + (i & 1)
            print(ret)
        return ret
        

        