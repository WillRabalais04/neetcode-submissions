class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)

        for s in strs:
            cc = [-1] * 26
            for c in s:
                cc[ord(c) - ord("a")] += 1
            ans[tuple(cc)].append(s)
        return ans.values()