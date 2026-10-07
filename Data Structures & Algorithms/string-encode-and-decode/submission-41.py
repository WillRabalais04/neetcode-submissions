class Solution:

    def encode(self, strs: List[str]) -> str:
        
        if not strs:
            ret = "EMPTY"
        else:
            ret = "-".join(strs)
            idx = 0
            while idx < len(ret):
                if (ret[idx] == "-"):
                    idx += 1
                    continue
                else:
                    curr = str(ord(ret[idx])) + ","

                ret = ret[:idx] + curr + ret[idx + 1:]
                idx += len(curr)
            
            ret = ret[:-1]
        return ret



    def decode(self, s: str) -> List[str]:

        if s == "EMPTY":
            return []

        s = s.split("-")

        if s == ['']:
            return s
        else:
            ret = []
            for word in s:
                word = word.split(",")
                word_string = ""
                for char in word:
                    if char != '':
                        word_string += (chr(int(char)))
                    
                ret.append(word_string)
            return ret
