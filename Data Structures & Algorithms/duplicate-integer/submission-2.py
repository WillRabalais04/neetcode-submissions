class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        entrs = {}
        for entry in nums:
            entrs[entry] = 0

        for entry in nums:
            print(entry)
            print(entrs[entry])
            entrs[entry] += 1;

        for entry in entrs:
            if entrs[entry] > 1:
                return True

        return False
