class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(s1):
            if len(s1) == 0:
                return False
            for i in range(len(s1) // 2):
                if s1[i] != s1[-(i+1)]:
                    return False
            return True
        
        ret = []

        def dfs(idx, path):
            print(f"path: {path}")
            if idx == len(s):
                ret.append(path[:])
                return
            for end in range(idx+1, len(s)+1):
                substr = s[idx:end]
                if isPalindrome(substr):
                    dfs(end, path + [substr])
        dfs(0,[])

        return ret
