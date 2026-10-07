class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        ret = []
        print(candidates)

        def dfs(idx, cs, path):
            if cs == target:
                ret.append(path[:])
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if cs + candidates[i] > target:
                    break
                path.append(candidates[i])
                dfs(i + 1, cs + candidates[i], path)
                path.pop()
        
        
        dfs(0,0,[])
        return ret