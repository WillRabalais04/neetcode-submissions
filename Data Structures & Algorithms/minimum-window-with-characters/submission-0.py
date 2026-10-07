class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #  A-Z    a-z
        # 65-90, 97-122
        # indices 0-25 are upper case, indices 25-51 are lowercase 
        def getIdx(c):
            idx = ord(c) - 65
            if ord(c) > 96: 
                idx -= 7
            return idx

        def makeCharTable(arr): # O(n) 
            ret = [0] * 52
            for i in range(len(arr)):
                ret[getIdx(arr[i])] += 1
            return ret

        def verifyCharTable(ct, ts): # O(1)?
            for i in range(52):
                if ct[i] < ts[i]:
                    return False
            return True

        ts = makeCharTable(t)
        ss = makeCharTable(s) 

        if not verifyCharTable(ss,ts):
            return ""
        
        l,r = 0, len(s) - 1
        while l <= r and l < len(s) - 1 and r > 0:
            lidx, ridx = getIdx(s[l]), getIdx(s[r])
            print("l " + str(l) + " | r: " + str(r))
            # print("ss[lidx]: " + str(ss[lidx]) + "ss[ridx]: " + str(ss[ridx]))
            if ss[lidx] > ts[lidx]:
                ss[lidx] -= 1
                l += 1
            elif ss[ridx] > ts[ridx]:
                ss[ridx] -= 1
                r -= 1
            else:
                break

                
            
        return str(s[l:r + 1])



        