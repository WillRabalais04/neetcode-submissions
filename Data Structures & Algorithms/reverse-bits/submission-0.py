class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(32):
            ret |= (((1 << i) & n) >> i) << (31 - i)

        return ret
        