class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord("A")] += 1
        max_heap = [-f for f in freq if f > 0]
        heapq.heapify(max_heap)
        
        max_freq = -max_heap[0]
        # trailing_i = abs(n - min_freq) 
        num_with_max_freq = sum(1 for f in freq if f == max_freq)

        max_freq = max(freq)
        num_with_max = freq.count(max_freq)

        # imagine blocks of length (n+1), repeated (max_freq - 1) times
        # then splice in all tasks with max frequency
        idle_layout = (max_freq - 1) * (n + 1) + num_with_max

        # total cycles = min between "idle layout" and "just tasks"
        return max(len(tasks), idle_layout)
        # ret = len(tasks) * (n + 1)
        # heapq.heappop(max_heap) # start with 2nd most freq
        # subsumed = 0
        # for i in range(n):
        #     subsumed += 1
        #     print(ret)
        #     if len(max_heap) < 1:
        #         break
        #     ret += (heapq.heappop(max_heap) * (n + 1))
        # print(f"ret: {ret} | least freq elem: {min_freq} | trailing i's: {(n+1) - min_freq}")
        # ret -= subsumed
        # return ret

# n=3
# "A","A","A","B","C"


# # min_cycles = 3 * 4 = 12
# # max_cycles = 5*4  = 20

# aiii aiii aiii biii ciii = 20
# abii aiii aiii ciii = 16
# abci aiii aiii = 12 - 3 = 9

# trailing i's = (n + 1) - lowest freq


# # n = 2
# # aaaaa bbbb ccc
# # 5 4 3
# n=2
# aaa bbb ccc d 
# aii aii aii bii bii bii cii cii cii dii
# abi abi abi cii cii dii
# abc abc abc dii

# aaa bbb ccc ddd eee f
# aii aii aii bii bii bii cii cii cii dii dii dii eii eii eii fii
# abi abi abi cii cii dii
# abc abc abc dii

# # # min_cycles = maxf * (n + 1) = 15 - idle at the end (1) = 14
# # # max_cycles = len(tasks) * (n + 1)  = 

# # abc abc abc abi aii = 15 -2 = 13
# # aii aii aii aii aii bii bii bii bii cii cii cii = 36 - 2 = 34
# # splicing b
# # abi abi abi abi aii cii cii cii = 24 - 2 = 22
# # splicing c | subtract (freq[c] * (n + 1))
# # abc abc abc abi aii = 15 - 2 = 13
# # ________
# # n = 2
# # aaa bb c
# # maxc = aii aii aii bii bii cii = 15
# # minc = abc abi aii
# # ________
# # n = 2
# # aaa bbb c
# # maxc = aii aii aii bii bii cii = 15
# # minc = abc abi abi 
# # 9


# xii xii yii yii 

# xyi xyi


# aaa bbb

# aii aii aii bii bii bii

# abi abi abi