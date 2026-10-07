class Solution:
    def partitionLabels(self, s: str) -> List[int]:
    
        last_idx = {}
        for i,c in enumerate(s):
            last_idx[c] = i
        
        ret = []
        size = end = 0
        for i,c in enumerate(s):
            size += 1
            end = max(end, last_idx[c])

            if i == end:
                ret.append(size)
                size = 0

        return ret