class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for x in nums:
            if not x in freq:
                freq[x] = 1
            else:
                freq[x] += 1
        
        freq_sorted = sorted(freq, key=freq.get)
        print(freq_sorted)

        return freq_sorted[len(freq_sorted)-k:]
