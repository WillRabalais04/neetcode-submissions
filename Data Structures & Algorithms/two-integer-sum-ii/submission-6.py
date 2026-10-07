class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        Map = defaultdict()
        ret = []

        for idx in range (0, len(numbers)):
            Map[numbers[idx]] = idx + 1;
        
        for idx in range (0, len(numbers)):
            complement = target - numbers[idx]
            if complement in Map:
                ret = [idx + 1, Map[complement]]
                break
        
        return ret

        