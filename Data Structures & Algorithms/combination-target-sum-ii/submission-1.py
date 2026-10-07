class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ret = []
        candidates.sort()

        def dfs(idx,path,total):
            if total == target:
                ret.append(path.copy())
                return 
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i-1] == candidates[i]:
                    continue
                if total + candidates[i] > target:
                    break
                path.append(candidates[i])
                dfs(i + 1, path, total + candidates[i])
                path.pop()

        dfs(0,[],0);
        return ret