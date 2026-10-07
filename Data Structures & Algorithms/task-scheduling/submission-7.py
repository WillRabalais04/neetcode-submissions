class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord("A")] += 1

        max_freq = max(freq)
        num_gaps = (max_freq - 1)
        seq_length = (n + 1)
        remainder = freq.count(max_freq)

        max_length = num_gaps * seq_length + remainder
        return max(max_length, len(tasks))

        