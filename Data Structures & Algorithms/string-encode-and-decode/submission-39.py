class Solution:

    def encode(self, strs: List[str]) -> str:
        
        if not strs:
            ret = "EMPTY"
        else:
            ret = "-".join(strs)
            print(ret)
            idx = 0
            while idx < len(ret):
                curr = str(ord(ret[idx]))
                print(curr)
                if (curr == str(ord("-"))):
                    curr = "|"
                else:
                    curr += ","
                ret = ret[:idx] + curr + ret[idx + 1:]
                idx += len(curr)
            
            ret = ret[:-1]
        return ret



    def decode(self, s: str) -> List[str]:

        print(s)

        if s == "EMPTY":
            return []

        s = s.split("|")

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
