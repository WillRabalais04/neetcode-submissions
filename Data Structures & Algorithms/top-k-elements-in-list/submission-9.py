class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        inv_freq = [[] for _ in range(len(nums) + 1)]
        # print(f"freq.keys():{freq.keys()}")
        for n in freq.keys():
            # print(f"n:{n} | freq[n]: {freq[n]}\n")
            inv_freq[freq[n]].append(n)
        print(f"inv_freq:{inv_freq}")
        ret = list()
        for idx in range(len(inv_freq) -1, -1, -1):
            # print(f"inv_freq[idx]:{inv_freq[idx]}")
            if len(inv_freq[idx]) > 0:
                ret += inv_freq[idx]
            if len(ret) >= k:
                break
        return ret
