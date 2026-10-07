class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        max_streak = 0

        for num in num_set:
            if num - 1 not in num_set:  # Only start from beginning of sequences
                current = num
                streak = 1
                while current + 1 in num_set:
                    current += 1
                    streak += 1
                max_streak = max(max_streak, streak)
        
        return max_streak



        