class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        Map = defaultdict()
        ret = []

        for idx in range (0, len(numbers)):
            Map[numbers[idx]] = idx + 1;
        
        for idx in range (0, len(numbers)):
            # print("Target: '" + str(target) + "' idx: " + str(idx) + "' numbers[Map[num]]: '" + str(numbers[Map[(idx)]]) + "'" )
            if (target - numbers[idx]) in Map:
                ret = [idx + 1, Map[target - numbers[idx]]]
                break
        
        return ret

        