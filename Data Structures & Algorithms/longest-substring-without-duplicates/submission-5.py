class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        if not s:
            return 0

        l,r = 0,0
        
        sc = set()
        ml = 0


        while r < len(s):
            curr = s[r]
            if not curr in sc:
                r += 1
                sc.add(curr)
                ml = max(ml,r -l)
            else: 
                sc.remove(s[l])
                l += 1
            print("l: " + str(l) + " | r: " + str(r))
            print(str(sc) + " | ml: " + str(ml))
        return ml
                
        