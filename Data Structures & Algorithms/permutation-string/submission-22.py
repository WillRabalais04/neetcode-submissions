class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        def get_freaky_arr(s):
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            return freq

        s1_freq = get_freaky_arr(s1)
        window_freq = get_freaky_arr(s2[:len(s1)])

        if window_freq == s1_freq:
            return True

        freq = get_freaky_arr(s1)
        for i in range(len(s1), len(s2)):
            l = ord(s2[i - len(s1)]) - ord('a')
            r = ord(s2[i]) - ord('a')
            window_freq[l] -= 1
            window_freq[r] += 1

            if window_freq == s1_freq:
                return True
            
        return False



        