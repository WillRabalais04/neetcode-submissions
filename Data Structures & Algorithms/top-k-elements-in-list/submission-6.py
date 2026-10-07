class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)
        for num in nums: freq[num] += 1
        vals = sorted(freq, key=freq.get,)
        return vals[-k:]



        