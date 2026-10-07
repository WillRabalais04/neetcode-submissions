class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sl = {x: 0 for x in list(s)}
        tl = {x: 0 for x in list(t)}

        for x in list(s):
            sl[x] +=1

        for x in list(t):
            tl[x] +=1
        
        return sl == tl
            
        