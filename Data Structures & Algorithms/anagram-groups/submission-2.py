class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        ana = {''.join(sorted(x)): [] for x in strs}

        for i,n in enumerate(strs):
            ana[''.join(sorted(n))].append(i)

        ret = list()

        for x in ana.values():
            l2 = list()
            for y in x:
                l2.append(strs[y])
            ret.append(l2)

        return ret
            

        