class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {x: 0 for x in nums}
        for x in nums:
            freq[x] +=1

        return sorted(freq,key = freq.get)[-k:]