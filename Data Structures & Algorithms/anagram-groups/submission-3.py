class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ret = {''.join(sorted(x)) : [] for x in strs}

        for word in strs:
            scrambled = ''.join(sorted(word))
            (ret[scrambled]).append(word)
            
        return ret.values()
        