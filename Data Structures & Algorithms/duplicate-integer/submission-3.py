class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dict = {}
        for x in nums:
            if x in dict:
                return True
            dict[x] = True
        return False

