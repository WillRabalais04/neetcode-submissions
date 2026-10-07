class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        count = Counter(s)
        ret = []
        lpi = -1
        curr = set()

        for i in range(len(s)):
            curr.add(s[i])
            count[s[i]] -= 1
            if count[s[i]] == 0:
                curr.remove(s[i])
                if len(curr) == 0:
                    print(f"i: {i} | s[i]: {s[i]}")
                    ret.append(i - lpi)
                    lpi = i

        return ret


        