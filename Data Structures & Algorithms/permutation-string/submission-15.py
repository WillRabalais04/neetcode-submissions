class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        gc1 = {}
        for x in s1:
            gc1[x] = gc1.get(x, 0) + 1
        gc2 = {}

        for r in range(len(s2)):
            gc2[s2[r]] = gc2.get(s2[r], 0) + 1

            if (s2[l] not in s1 or gc2[s2[l]] != gc1[s2[l]] or (r - l + 1) > len(s1)) and l < len(s2) :
                gc2[s2[l]] -= 1
                if gc2[s2[l]] == 0:
                    gc2.pop(s2[l])
                l += 1

            if gc1 == gc2: # kind of slow but whatever
                return True

        return False
    