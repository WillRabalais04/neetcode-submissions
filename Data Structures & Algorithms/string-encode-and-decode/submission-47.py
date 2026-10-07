class Solution:

    def encode(self, strs: List[str]) -> str:

        return ''.join(f"{len(s)}|{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        print(s)
        ret = []
        idx = 0
        while idx < len(s):
            l = int(s[idx:s.index("|", idx)])
            idx += len(str(l)) + 1
            word = s[idx:idx + l]
            print(word)
            ret.append(word)
            idx += l
        return ret
