class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ret = []
        candidates.sort()

        def dfs(i,p,t):
            if t == target:
                ret.append(p.copy())
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if t + candidates[j] > target:
                    break
                p.append(candidates[j])
                dfs(j + 1,p, t + candidates[j])
                p.pop()
        
        dfs(0, [], 0)
        return ret