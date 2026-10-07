class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        print(candidates)
        ret = []
        def dfs(s, idx, arr):
            print(arr)
            if s == target:
                ret.append(arr[:]) # arr[:] makes a shallow copy
                return
            if s > target:
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]: 
                    continue
                dfs(s + candidates[i], i + 1, arr + [candidates[i]])

        dfs(0,0,[])

        return ret