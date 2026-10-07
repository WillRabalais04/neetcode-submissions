class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        comp = []
        ret = []
        for x in numbers:
            comp.append(target - x)
        for i in range(len(numbers)):
            c = comp[i]
            if (c in numbers and numbers.index(c) != i):
                ret = [i+1,numbers.index(c)+1]
                break
        return ret


        