class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        
        mappings = {
            "2" :["a","b","c"],
            "3" :["d","e","f"],
            "4" :["g","h","i"],
            "5" :["j","k","l"],
            "6" :["m","n","o"],
            "7" :["p","q","r","s"],
            "8" :["t","u","v"],
            "9" :["w","x","y","z"]
        }
        if len(digits) == 0:
            return []
        
        ret = []
        def dfs(idx, path):
            if idx == len(digits):
                ret.append("".join(path))
                return
            if idx > len(digits):
                return

            for letter in mappings[digits[idx]]:
                dfs(idx + 1, path + [letter])

        dfs(0, [])
        return ret


        

        