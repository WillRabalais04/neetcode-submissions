class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(32):
            ret |= ((n >> i) & 1) << (31 - i)
        return ret
        