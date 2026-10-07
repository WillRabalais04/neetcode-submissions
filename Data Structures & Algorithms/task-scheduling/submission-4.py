class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord("A")] += 1
        max_heap = [-f for f in freq if f > 0]
        heapq.heapify(max_heap)
        
        max_freq = max(freq)
        num_with_max = freq.count(max_freq)

        idle_layout = (max_freq - 1) * (n + 1) + num_with_max

        return max(len(tasks), idle_layout)
