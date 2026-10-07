class Solution:
    def to_dict(self, l) -> dict:
        ret = {}
        for char in l:
            curr_count = 1
            if char in ret:
                curr_count = ret.get(char) + 1
            ret[char] = curr_count
        return ret

    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = self.to_dict(list(s))
        t_dict = self.to_dict(list(t))
        return t_dict == s_dict


  
            
        