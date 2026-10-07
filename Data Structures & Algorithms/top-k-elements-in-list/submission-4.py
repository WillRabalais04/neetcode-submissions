class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = defaultdict(int)
        for x in nums:
            f[x] +=1

        print(f)
        
        f = sorted(f.items(), key = lambda item: item[1], reverse = True)
        ret = [x for (x,y) in f]
        return ret[:k]
            
        