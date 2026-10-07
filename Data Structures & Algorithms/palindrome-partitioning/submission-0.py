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
            if idx == len(s):
                print(f"ret path: {path}")
                ret.append(path[:])
                return
            for end in range(idx+1, len(s)+1):
                substr = s[idx:end]
                print(f"path: {path} | substr: {substr}")
                if isPalindrome(substr):
                    dfs(end, path + [substr])
                print()
        dfs(0,[])

        return ret



        # dfs depth 1: a a b -> [a,a,b]
        # dfs depth 2: aa, ab, ba -> [a,a]
