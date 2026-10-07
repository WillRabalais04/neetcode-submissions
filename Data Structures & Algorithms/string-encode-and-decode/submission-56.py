class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""  
        strs = ["*".join([str(ord(c) + (i % 2 - 1) * 10 + 69) for (i,c) in enumerate(s)]) for s in strs]
        return "#" + "-".join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        ret = list()
        for s in  s[1:].split("-"):
            encoded = s.split("*")
            decoded = ''
            for i,c in enumerate(encoded):
                if c == '':
                    continue
                decoded += (chr((int(c)- 69) - (i % 2 - 1) * 10))
            ret.append(decoded)

        return ret


