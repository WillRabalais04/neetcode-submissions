class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1freq = [0] * 26
        for c in s1:
            s1freq[ord(c) - ord('a')] += 1
        
        l,r = 0, len(s1)
        
        windowfreq = [0] * 26
        for i in range(r):
            windowfreq[ord(s2[i]) - ord('a')] += 1
        
        print(s1freq)
        while r <= len(s2):
            if windowfreq == s1freq:
                return True
            if r == len(s2):
                break
            windowfreq[ord(s2[l]) - ord('a')] -= 1
            windowfreq[ord(s2[r]) - ord('a')] += 1
            l += 1
            r += 1
        return False



        