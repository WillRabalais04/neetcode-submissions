class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        def getFreakArr(s):
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            return freq

        freq = getFreakArr(s1)
        c = 0
        while (c + len(s1) - 1) < len(s2):
            if s2[c] in s1:
                windowfreq = getFreakArr(s2[c: c + len(s1)])
                print(s2[c: c + len(s1)])
                if windowfreq == freq:
                    return True
            c += 1
            
        return False



        