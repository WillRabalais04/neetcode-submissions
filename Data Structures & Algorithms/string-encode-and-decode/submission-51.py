class Solution:

    def encode(self, strs: List[str]) -> str:
        strs = ["*".join([str(ord(c) + (i % 2 - 1) * 10 + 69) for (i,c) in enumerate(s)]) for s in strs]
        return "-".join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return [""]
        strs = s.split("-")
        ret = list()
        for s in strs:
            encoded = s.split("*")
            decoded = ""
            for i,c in enumerate(encoded):
                if c == '':
                    continue
                decoded += (chr((int(c)- 69) - (i % 2 - 1) * 10))
            ret.append(decoded)

        return ret


